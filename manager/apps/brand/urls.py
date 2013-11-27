from django.conf.urls import patterns, url
from manager.apps.brand.views import BrandListView
from manager.apps.brand.views import BrandView

urlpatterns = patterns(
    '',
    url(r'^$', BrandListView.as_view(), name='brandlist'),
    url(r'^owner', OwnerListView.as_view(), name='ownerlist'),
    #regular expression for a BSIN
    url(r'^(?P<bsin>[1-9A-NP-Z]{6})', BrandView.as_view(), name='brand'),
)
