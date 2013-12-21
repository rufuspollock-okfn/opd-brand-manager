from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from manager.apps.brand.api import BrandResource  # [#58] , BrandOwnerResource
from django.conf import settings

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(BrandResource())
# Postponed in ticket #58
#v1_api.register(BrandOwnerResource())

urlpatterns = patterns(
    '',

    url(r'^api/', include(v1_api.urls)),
    url(r'', include('manager.apps.main.urls')),
    url(r'', include('manager.apps.brand.urls')),

    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('', (
        r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}))
