from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect

from shortcut import views

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('shortcut/')),
    url(r'^shortcut/$', views.MakeShortcut.as_view(), name='MakeShortcut'),
    url(r'^shortcut/(?P<appid>[0-9]+)/$', views.Shortcut.as_view(name='foo')),
    url(r'^admin/', admin.site.urls),
]
