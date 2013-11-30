from django.conf.urls import patterns, url
from manager.apps.brand.views import BrandListView, BrandView
from manager.apps.brand.views import OwnerListView, OwnerView
from manager.apps.brand.views import BrandProposalView, BrandProposedView

urlpatterns = patterns(
    '',
    url(r'^brand/$', BrandListView.as_view(), name='brandlist'),
    url(r'^brand/(?P<bsin>[1-9A-NP-Z]{6})', BrandView.as_view(), name='brand'),
    url(r'^brand/new/$', BrandProposalView.as_view(), name='brandproposal'),
    url(r'^brand/proposed/$', BrandProposedView.as_view(),
        name='brandproposed'),

    url(r'^owner/$', OwnerListView.as_view(), name='ownerlist'),
    url(r'^owner/(?P<cd>[1-9]+)', OwnerView.as_view(), name='owner'),
)
