from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from import_export.admin import ImportMixin, ImportExportMixinBase
from import_export.formats import base_formats
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_str
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import path, reverse

from django.views.decorators.http import require_POST

from django.conf import settings
from django.contrib.auth import get_permission_codename
from django.utils.module_loading import import_string
from import_export.forms import ConfirmImportForm

from shop.import_export.resources import ProductResourceMain, ProductResourceSecondary
from import_export.resources import modelresource_factory

from import_export.tmp_storages import TempFolderStorage

from import_export.formats import base_formats
from import_export.signals import post_export, post_import

from import_export.results import RowResult
from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.contrib.contenttypes.models import ContentType
from django.contrib import admin, messages


class ImportForm(forms.Form):
    import_file = forms.FileField(
        label=_('File to import')
    )
    # input_format = forms.ChoiceField(
    #     label=_('Format'),
    #     choices=(),
    #     )

    # def __init__(self, import_formats, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     choices = []
    #     for i, f in enumerate(import_formats):
    #         choices.append((str(i), f().get_title(),))
    #     if len(import_formats) > 1:
    #         choices.insert(0, ('', '---'))
    #
    #     self.fields['input_format'].choices = choices


class MyImportMixin(ImportExportMixinBase):
    import_template_name_first = 'shop/admin/import_export/import_first.html'
    import_template_name_second = 'shop/admin/import_export/import_second.html'
    change_list_template = 'shop/admin/import_export/change_list_import.html'

    resource_class_first = None
    resource_class_second = None

    from_encoding = "utf-8"
    skip_admin_log = None

    tmp_storage_class = None

    def get_skip_admin_log(self):
        if self.skip_admin_log is None:
            return getattr(settings, 'IMPORT_EXPORT_SKIP_ADMIN_LOG', False)
        else:
            return self.skip_admin_log

    def get_tmp_storage_class(self):
        if self.tmp_storage_class is None:
            tmp_storage_class = getattr(
                settings, 'IMPORT_EXPORT_TMP_STORAGE_CLASS', TempFolderStorage,
            )
        else:
            tmp_storage_class = self.tmp_storage_class

        if isinstance(tmp_storage_class, str):
            tmp_storage_class = import_string(tmp_storage_class)
        return tmp_storage_class

    def has_import_permission(self, request):
        """
        Returns whether a request has import permission.
        """
        IMPORT_PERMISSION_CODE = getattr(settings, 'IMPORT_EXPORT_IMPORT_PERMISSION_CODE', None)
        if IMPORT_PERMISSION_CODE is None:
            return True

        opts = self.opts
        codename = get_permission_codename(IMPORT_PERMISSION_CODE, opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def get_urls(self):
        urls = super().get_urls()
        info = self.get_model_info()
        my_urls = [
            path('process_import_first/',
                 self.admin_site.admin_view(self.process_import_first),
                 name='%s_%s_process_import_first' % info),
            path('import_first/',
                 self.admin_site.admin_view(self.import_action_first),
                 name='%s_%s_import_first' % info),
            path('process_import_second/',
                 self.admin_site.admin_view(self.process_import_second),
                 name='%s_%s_process_import_second' % info),
            path('import_second/',
                 self.admin_site.admin_view(self.import_action_second),
                 name='%s_%s_import_second' % info),
        ]
        return my_urls + urls

    def get_resource_kwargs(self, request, *args, **kwargs):
        return {}



    def get_resource_class_first(self):
        """Returns ResourceClass"""
        if not self.resource_class_first:
            return modelresource_factory(self.model)
        else:
            return self.resource_class_first

    def get_import_resource_class_first(self):
        """
        Returns ResourceClass to use for import.
        """
        return self.get_resource_class_first()

    def get_resource_class_second(self):
        """Returns ResourceClass"""
        if not self.resource_class_second:
            return modelresource_factory(self.model)
        else:
            return self.resource_class_second

    def get_import_resource_class_second(self):
        """
        Returns ResourceClass to use for import.
        """
        return self.get_resource_class_second()

    def get_import_resource_kwargs(self, request, *args, **kwargs):
        """Prepares/returns kwargs used when initializing Resource"""
        return self.get_resource_kwargs(request, *args, **kwargs)


    @method_decorator(require_POST)
    def process_import_first(self, request, *args, **kwargs):
        """
        Perform the actual import action (after the user has confirmed the import)
        """
        if not self.has_import_permission(request):
            raise PermissionDenied

        form_type = self.get_confirm_import_form()
        confirm_form = form_type(request.POST)
        if confirm_form.is_valid():
            input_format = base_formats.XLS()
            tmp_storage = self.get_tmp_storage_class()(name=confirm_form.cleaned_data['import_file_name'])
            data = tmp_storage.read(input_format.get_read_mode())
            if not input_format.is_binary() and self.from_encoding:
                data = force_str(data, self.from_encoding)
            dataset = input_format.create_dataset(data)

            result = self.process_dataset_first(dataset, confirm_form, request, *args, **kwargs)

            tmp_storage.remove()

            return self.process_result(result, request)

    def process_dataset_first(self, dataset, confirm_form, request, *args, **kwargs):

        res_kwargs = self.get_import_resource_kwargs(request, form=confirm_form, *args, **kwargs)
        resource = self.get_import_resource_class_first()(**res_kwargs)

        imp_kwargs = self.get_import_data_kwargs(request, form=confirm_form, *args, **kwargs)
        return resource.import_data(dataset,
                                    dry_run=False,
                                    raise_errors=True,
                                    file_name=confirm_form.cleaned_data['original_file_name'],
                                    user=request.user,
                                    **imp_kwargs)

    def process_import_second(self, request, *args, **kwargs):
        """
        Perform the actual import action (after the user has confirmed the import)
        """
        if not self.has_import_permission(request):
            raise PermissionDenied

        form_type = self.get_confirm_import_form()
        confirm_form = form_type(request.POST)
        if confirm_form.is_valid():
            input_format = base_formats.XLS()
            tmp_storage = self.get_tmp_storage_class()(name=confirm_form.cleaned_data['import_file_name'])
            data = tmp_storage.read(input_format.get_read_mode())
            if not input_format.is_binary() and self.from_encoding:
                data = force_str(data, self.from_encoding)
            dataset = input_format.create_dataset(data)

            result = self.process_dataset_second(dataset, confirm_form, request, *args, **kwargs)

            tmp_storage.remove()

            return self.process_result(result, request)

    def process_dataset_second(self, dataset, confirm_form, request, *args, **kwargs):

        res_kwargs = self.get_import_resource_kwargs(request, form=confirm_form, *args, **kwargs)
        resource = self.get_import_resource_class_second()(**res_kwargs)

        imp_kwargs = self.get_import_data_kwargs(request, form=confirm_form, *args, **kwargs)
        return resource.import_data(dataset,
                                    dry_run=False,
                                    raise_errors=True,
                                    file_name=confirm_form.cleaned_data['original_file_name'],
                                    user=request.user,
                                    **imp_kwargs)

    def process_result(self, result, request):
        self.generate_log_entries(result, request)
        self.add_success_message(result, request)
        post_import.send(sender=None, model=self.model)

        url = reverse('admin:%s_%s_changelist' % self.get_model_info(),
                      current_app=self.admin_site.name)
        return HttpResponseRedirect(url)

    def generate_log_entries(self, result, request):
        if not self.get_skip_admin_log():
            # Add imported objects to LogEntry
            logentry_map = {
                RowResult.IMPORT_TYPE_NEW: ADDITION,
                RowResult.IMPORT_TYPE_UPDATE: CHANGE,
                RowResult.IMPORT_TYPE_DELETE: DELETION,
            }
            content_type_id = ContentType.objects.get_for_model(self.model).pk
            for row in result:
                if row.import_type != row.IMPORT_TYPE_ERROR and row.import_type != row.IMPORT_TYPE_SKIP:
                    LogEntry.objects.log_action(
                        user_id=request.user.pk,
                        content_type_id=content_type_id,
                        object_id=row.object_id,
                        object_repr=row.object_repr,
                        action_flag=logentry_map[row.import_type],
                        change_message=_("%s through import_export" % row.import_type),
                    )

    def get_import_context_data(self, **kwargs):
        return self.get_context_data(**kwargs)

    def get_context_data(self, **kwargs):
        return {}

    def add_success_message(self, result, request):
        opts = self.model._meta

        success_message = _('Import finished, with {} new and ' \
                            '{} updated {}.').format(result.totals[RowResult.IMPORT_TYPE_NEW],
                                                      result.totals[RowResult.IMPORT_TYPE_UPDATE],
                                                      opts.verbose_name_plural)

        messages.success(request, success_message)

    def get_import_form(self):
        """
        Get the form type used to read the import format and file.
        """
        return ImportForm

    def get_confirm_import_form(self):
        """
        Get the form type (class) used to confirm the import.
        """
        return ConfirmImportForm

    def get_form_kwargs(self, form, *args, **kwargs):
        """
        Prepare/returns kwargs for the import form.

        To distinguish between import and confirm import forms,
        the following approach may be used:

            if isinstance(form, ImportForm):
                # your code here for the import form kwargs
                # e.g. update.kwargs({...})
            elif isinstance(form, ConfirmImportForm):
                # your code here for the confirm import form kwargs
                # e.g. update.kwargs({...})
            ...
        """
        return kwargs

    def get_import_data_kwargs(self, request, *args, **kwargs):
        """
        Prepare kwargs for import_data.
        """
        form = kwargs.get('form')
        if form:
            kwargs.pop('form')
            return kwargs
        return {}

    def write_to_tmp_storage(self, import_file, input_format):
        tmp_storage = self.get_tmp_storage_class()()
        data = bytes()
        for chunk in import_file.chunks():
            data += chunk

        tmp_storage.save(data, input_format.get_read_mode())
        return tmp_storage

    def import_action_first(self, request, *args, **kwargs):
        """
        Perform a dry_run of the import to make sure the import will not
        result in errors.  If there where no error, save the user
        uploaded file to a local temp file that will be used by
        'process_import' for the actual import.
        """
        if not self.has_import_permission(request):
            raise PermissionDenied

        context = self.get_import_context_data()

        form_type = self.get_import_form()
        form_kwargs = self.get_form_kwargs(form_type, *args, **kwargs)
        form = form_type(request.POST or None,
                         request.FILES or None,
                         **form_kwargs)

        if request.POST and form.is_valid():
            input_format = base_formats.XLS()
            import_file = form.cleaned_data['import_file']
            # first always write the uploaded file to disk as it may be a
            # memory file or else based on settings upload handlers
            tmp_storage = self.write_to_tmp_storage(import_file, input_format)

            # then read the file, using the proper format-specific mode
            # warning, big files may exceed memory
            try:
                data = tmp_storage.read(input_format.get_read_mode())
                if not input_format.is_binary() and self.from_encoding:
                    data = force_str(data, self.from_encoding)
                dataset = input_format.create_dataset(data)
            except UnicodeDecodeError as e:
                return HttpResponse(_(u"<h1>Imported file has a wrong encoding: %s</h1>" % e))
            except Exception as e:
                return HttpResponse(
                    _(u"<h1>%s encountered while trying to read file: %s</h1>" % (type(e).__name__, import_file.name)))

            # prepare kwargs for import data, if needed
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class_first()(**res_kwargs)

            # prepare additional kwargs for import_data, if needed
            imp_kwargs = self.get_import_data_kwargs(request, form=form, *args, **kwargs)
            result = resource.import_data(dataset, dry_run=True,
                                          raise_errors=False,
                                          file_name=import_file.name,
                                          user=request.user,
                                          **imp_kwargs)

            context['result'] = result

            if not result.has_errors() and not result.has_validation_errors():
                initial = {
                    'import_file_name': tmp_storage.name,
                    'original_file_name': import_file.name,
                    # 'input_format': form.cleaned_data['input_format'],
                    'input_format': input_format,
                }
                confirm_form = self.get_confirm_import_form()
                initial = self.get_form_kwargs(form=form, **initial)
                context['confirm_form'] = confirm_form(initial=initial)
        else:
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class_first()(**res_kwargs)

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Import")
        context['form'] = form
        context['opts'] = self.model._meta
        context['fields'] = [f.column_name for f in resource.get_user_visible_fields()]

        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.import_template_name_first], context)

    def import_action_second(self, request, *args, **kwargs):
        """
        Perform a dry_run of the import to make sure the import will not
        result in errors.  If there where no error, save the user
        uploaded file to a local temp file that will be used by
        'process_import' for the actual import.
        """
        if not self.has_import_permission(request):
            raise PermissionDenied

        context = self.get_import_context_data()

        form_type = self.get_import_form()
        form_kwargs = self.get_form_kwargs(form_type, *args, **kwargs)
        form = form_type(request.POST or None,
                         request.FILES or None,
                         **form_kwargs)

        if request.POST and form.is_valid():
            input_format = base_formats.XLS()
            import_file = form.cleaned_data['import_file']
            # first always write the uploaded file to disk as it may be a
            # memory file or else based on settings upload handlers
            tmp_storage = self.write_to_tmp_storage(import_file, input_format)

            # then read the file, using the proper format-specific mode
            # warning, big files may exceed memory
            try:
                data = tmp_storage.read(input_format.get_read_mode())
                if not input_format.is_binary() and self.from_encoding:
                    data = force_str(data, self.from_encoding)
                dataset = input_format.create_dataset(data)
            except UnicodeDecodeError as e:
                return HttpResponse(_(u"<h1>Imported file has a wrong encoding: %s</h1>" % e))
            except Exception as e:
                return HttpResponse(
                    _(u"<h1>%s encountered while trying to read file: %s</h1>" % (type(e).__name__, import_file.name)))

            # prepare kwargs for import data, if needed
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class_second()(**res_kwargs)

            # prepare additional kwargs for import_data, if needed
            imp_kwargs = self.get_import_data_kwargs(request, form=form, *args, **kwargs)
            result = resource.import_data(dataset, dry_run=True,
                                          raise_errors=False,
                                          file_name=import_file.name,
                                          user=request.user,
                                          **imp_kwargs)

            context['result'] = result

            if not result.has_errors() and not result.has_validation_errors():
                initial = {
                    'import_file_name': tmp_storage.name,
                    'original_file_name': import_file.name,
                    'input_format': input_format,
                }
                confirm_form = self.get_confirm_import_form()
                initial = self.get_form_kwargs(form=form, **initial)
                context['confirm_form'] = confirm_form(initial=initial)
        else:
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class_second()(**res_kwargs)

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Import")
        context['form'] = form
        context['opts'] = self.model._meta
        context['fields'] = [f.column_name for f in resource.get_user_visible_fields()]

        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.import_template_name_second], context)


    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['has_import_permission'] = self.has_import_permission(request)
        return super().changelist_view(request, extra_context)
