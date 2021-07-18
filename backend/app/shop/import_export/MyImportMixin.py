from django.template.response import TemplateResponse
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django import forms

class MyImportForm(forms.Form):
    import_file1 = forms.FileField(
        label=_('File to import')
        )

    import_file2 = forms.FileField(
        label=_('File to import')
        )
    input_format = forms.ChoiceField(
        label=_('Format'),
        choices=(),
        )

    def __init__(self, import_formats, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        for i, f in enumerate(import_formats):
            choices.append((str(i), f().get_title(),))
        if len(import_formats) > 1:
            choices.insert(0, ('', '---'))

        self.fields['input_format'].choices = choices

class MyImportMixin(ImportMixin):

    import_template_name = 'admin/import_export/import.html'

    def get_import_form(self):
        """
        Get the form type used to read the import format and file.
        """
        return MyImportForm

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_import()]

    def import_action(self, request, *args, **kwargs):


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
            pass

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
