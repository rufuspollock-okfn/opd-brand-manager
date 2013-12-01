from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from manager.apps.brand.api import BrandResource, BrandOwnerResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(BrandResource())
v1_api.register(BrandOwnerResource())

urlpatterns = patterns(
    '',

    url(r'^api/', include(v1_api.urls)),
    url(r'', include('manager.apps.main.urls')),
    url(r'', include('manager.apps.brand.urls')),

    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
