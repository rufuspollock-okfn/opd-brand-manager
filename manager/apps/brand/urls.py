from django.conf.urls import patterns, url
from manager.apps.brand.views import BrandListView

urlpatterns = patterns(
    '',
    url(r'^$', BrandListView.as_view(), name='brandlist'),
)
