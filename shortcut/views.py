from django.shortcuts import render
from django.template import Context
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView

from shortcut.forms import ShortcutForm

ICON_SHORTCUT_HTML = 'icon/shortcut.html'


class Shortcut(TemplateView):
    template_name = ICON_SHORTCUT_HTML
    name = None
    appid = None

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        if name:
            self.name = name

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(Shortcut, self).get_context_data(**kwargs)
        context.update({'name': self.name})
        return context


class MakeShortcut(View):
    template_name = 'icon/shortcut_form.html'

    def get(self, request, *args, **kwargs):
        form = ShortcutForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            appid = form.cleaned_data.get('appid')
            print(appid, name)
            shortcut_html = render_to_string(ICON_SHORTCUT_HTML, {"name": name, 'appid': appid})
            return render(request, self.template_name, {
                'form': form,
                'shortcut_html': shortcut_html,
            })
        else:
            return render(request, self.template_name, {'form': ShortcutForm()})



