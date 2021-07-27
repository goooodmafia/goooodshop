from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_str
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import path, reverse

from django.views.decorators.http import require_POST

from shop.import_export.resources import ProductResourceSecondary


class MyImportMixin(ImportMixin):
    # pass
    change_list_template = 'shop/admin/import_export/change_list_import.html'

    def get_urls(self):
        urls = super().get_urls()
        info = self.get_model_info()
        my_urls = [
            path('process_import/',
                 self.admin_site.admin_view(self.process_import),
                 name='%s_%s_process_import' % info),
            path('import_main/',
                 self.admin_site.admin_view(self.main_import_action),
                 name='%s_%s_import_main' % info),
            path('process_import/',
                 self.admin_site.admin_view(self.process_import),
                 name='%s_%s_process_import' % info),
            path('import_secondary/',
                 self.admin_site.admin_view(self.secondary_import_action),
                 name='%s_%s_import_secondary' % info),
        ]
        return my_urls + urls

    def main_import_action(self, request, *args, **kwargs):
        """
        Perform a dry_run of the import to make sure the import will not
        result in errors.  If there where no error, save the user
        uploaded file to a local temp file that will be used by
        'process_import' for the actual import.
        """
        if not self.has_import_permission(request):
            raise PermissionDenied

        context = self.get_import_context_data()

        import_formats = self.get_import_formats()
        form_type = self.get_import_form()
        form_kwargs = self.get_form_kwargs(form_type, *args, **kwargs)
        form = form_type(import_formats,
                         request.POST or None,
                         request.FILES or None,
                         **form_kwargs)

        if request.POST and form.is_valid():
            input_format = import_formats[
                int(form.cleaned_data['input_format'])
            ]()
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
                return HttpResponse(_(u"<h1>%s encountered while trying to read file: %s</h1>" % (type(e).__name__, import_file.name)))

            # prepare kwargs for import data, if needed
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class()(**res_kwargs)

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
                    'input_format': form.cleaned_data['input_format'],
                }
                confirm_form = self.get_confirm_import_form()
                initial = self.get_form_kwargs(form=form, **initial)
                context['confirm_form'] = confirm_form(initial=initial)
        else:
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class()(**res_kwargs)

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Import")
        context['form'] = form
        context['opts'] = self.model._meta
        context['fields'] = [f.column_name for f in resource.get_user_visible_fields()]

        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.import_template_name],
                                context)

    def secondary_import_action(self, request, *args, **kwargs):
        """
        Perform a dry_run of the import to make sure the import will not
        result in errors.  If there where no error, save the user
        uploaded file to a local temp file that will be used by
        'process_import' for the actual import.
        """
        if not self.has_import_permission(request):
            raise PermissionDenied

        context = self.get_import_context_data()

        import_formats = self.get_import_formats()
        form_type = self.get_import_form()
        form_kwargs = self.get_form_kwargs(form_type, *args, **kwargs)
        form = form_type(import_formats,
                         request.POST or None,
                         request.FILES or None,
                         **form_kwargs)

        if request.POST and form.is_valid():
            input_format = import_formats[
                int(form.cleaned_data['input_format'])
            ]()
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
                return HttpResponse(_(u"<h1>%s encountered while trying to read file: %s</h1>" % (type(e).__name__, import_file.name)))

            # prepare kwargs for import data, if needed
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class()(**res_kwargs)

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
                    'input_format': form.cleaned_data['input_format'],
                }
                confirm_form = self.get_confirm_import_form()
                initial = self.get_form_kwargs(form=form, **initial)
                context['confirm_form'] = confirm_form(initial=initial)
        else:
            res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
            resource = self.get_import_resource_class()(**res_kwargs)

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Import")
        context['form'] = form
        context['opts'] = self.model._meta
        context['fields'] = [f.column_name for f in resource.get_user_visible_fields()]

        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.import_template_name],
                                context)

    # def process_import(self, request, *args, **kwargs):
    #     super(MainImportMixin, self).process_import(request, *args, **kwargs)

    # def importmain_action(self, request, *args, **kwargs):
    #     print('importmain_action')
    #     super(MainImportMixin, self).import_action(request, args, kwargs)


# class SecondaryImportMixin(ImportMixin):
#
#     change_list_template = 'shop/admin/import_export/change_list_import_secondary.html'
#
#     def get_urls(self):
#         urls = super().get_urls()
#         info = self.get_model_info()
#         my_urls = [
#             path('process_import_secondary/',
#                  self.admin_site.admin_view(self.process_import),
#                  name='%s_%s_process_import_secondary' % info),
#             path('importsecondary/',
#                  self.admin_site.admin_view(self.import_action),
#                  name='%s_%s_importsecondary' % info),
#         ]
#         return my_urls + urls
#
#     # def importsecondary_action(self, request, *args, **kwargs):
#     #     print('importsecondary_action')
#     #     super(SecondaryImportMixin, self).import_action(request, *args, **kwargs)

# class MyImportForm(forms.Form):
#     import_file1 = forms.FileField(
#         label=_('File to import')
#         )
#
#     import_file2 = forms.FileField(
#         label=_('File to import')
#         )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

# def __init__(self, import_formats, *args, **kwargs):
#     super().__init__(*args, **kwargs)
# choices = []
# for i, f in enumerate(import_formats):
#     choices.append((str(i), f().get_title(),))
# if len(import_formats) > 1:
#     choices.insert(0, ('', '---'))
#
# self.fields['input_format'].choices = choices

# class MyImportMixinMain(ImportMixin):
#
#     import_template_name = 'admin/import_export/import.html'
#
#     def get_import_form(self):
#         """
#         Get the form type used to read the import format and file.
#         """
#         return MyImportForm
#
#     def get_import_formats(self):
#         formats = (
#             base_formats.XLS,
#         )
#         return [f for f in formats if f().can_import()]
#
#     @method_decorator(require_POST)
#     def process_import(self, request, *args, **kwargs):
#         """
#         Perform the actual import action (after the user has confirmed the import)
#         """
#         if not self.has_import_permission(request):
#             raise PermissionDenied
#
#         form_type = self.get_confirm_import_form()
#         confirm_form = form_type(request.POST)
#         if confirm_form.is_valid():
#             import_formats = self.get_import_formats()
#             # input_format = import_formats[
#             #     int(confirm_form.cleaned_data['input_format'])
#             # ]()
#             input_format = import_formats[0]()
#             tmp_storage = self.get_tmp_storage_class()(name=confirm_form.cleaned_data['import_file_name'])
#             data = tmp_storage.read(input_format.get_read_mode())
#             if not input_format.is_binary() and self.from_encoding:
#                 data = force_str(data, self.from_encoding)
#             dataset = input_format.create_dataset(data)
#
#             result = self.process_dataset(dataset, confirm_form, request, *args, **kwargs)
#
#             tmp_storage.remove()
#
#             return self.process_result(result, request)
#
#     def import_action(self, request, *args, **kwargs):
#
#
#         if not self.has_import_permission(request):
#             raise PermissionDenied
#         context = self.get_import_context_data()
#         import_formats = self.get_import_formats()
#         form_type = self.get_import_form()
#         form_kwargs = self.get_form_kwargs(form_type, *args, **kwargs)
#         # form = form_type(import_formats,
#         form = form_type(
#                          request.POST or None,
#                          request.FILES or None,
#                          **form_kwargs)
#
#         if request.POST and form.is_valid():
#             # input_format = base_formats.XLS,
#             print(import_formats)
#             input_format = import_formats[0]()
#
#             import_file = form.cleaned_data['import_file1']
#             # first always write the uploaded file to disk as it may be a
#             # memory file or else based on settings upload handlers
#             tmp_storage = self.write_to_tmp_storage(import_file, input_format)
#
#             # then read the file, using the proper format-specific mode
#             # warning, big files may exceed memory
#             try:
#                 data = tmp_storage.read(input_format.get_read_mode())
#                 if not input_format.is_binary() and self.from_encoding:
#                     data = force_str(data, self.from_encoding)
#                 dataset = input_format.create_dataset(data)
#             except UnicodeDecodeError as e:
#                 return HttpResponse(_(u"<h1>Imported file has a wrong encoding: %s</h1>" % e))
#             except Exception as e:
#                 return HttpResponse(
#                     _(u"<h1>%s encountered while trying to read file: %s</h1>" % (type(e).__name__, import_file.name)))
#
#             # prepare kwargs for import data, if needed
#             res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
#             resource = self.get_import_resource_class()(**res_kwargs)
#
#             # prepare additional kwargs for import_data, if needed
#             imp_kwargs = self.get_import_data_kwargs(request, form=form, *args, **kwargs)
#             result = resource.import_data(dataset, dry_run=True,
#                                           raise_errors=False,
#                                           file_name=import_file.name,
#                                           user=request.user,
#                                           **imp_kwargs)
#
#             context['result'] = result
#
#             if not result.has_errors() and not result.has_validation_errors():
#                 initial = {
#                     'import_file_name': tmp_storage.name,
#                     'original_file_name': import_file.name,
#                     'input_format': base_formats.XLS
#                               # form.cleaned_data['input_format'],
#                 }
#                 confirm_form = self.get_confirm_import_form()
#                 initial = self.get_form_kwargs(form=form, **initial)
#                 context['confirm_form'] = confirm_form(initial=initial)
#
#         else:
#             res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
#             resource = self.get_import_resource_class()(**res_kwargs)
#
#         context.update(self.admin_site.each_context(request))
#
#         context['title'] = _("Import")
#         context['form'] = form
#         context['opts'] = self.model._meta
#         context['fields'] = [f.column_name for f in resource.get_user_visible_fields()]
#
#         request.current_app = self.admin_site.name
#         return TemplateResponse(request, [self.import_template_name],
#                                 context)
