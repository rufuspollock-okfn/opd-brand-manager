from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns(
    '',

    # Subsite configuration http://domain.tld/dir/
    url(settings.SUBSITE, include('manager.subsite_urls')),
)
