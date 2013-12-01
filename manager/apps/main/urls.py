from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from manager.apps.main.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/$', TemplateView.as_view(template_name='main/api.jade'),
        name='api'),
)
