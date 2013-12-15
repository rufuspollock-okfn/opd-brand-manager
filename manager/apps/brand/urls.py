from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from manager.apps.brand.views import BrandListView, BrandView
# Postponed in ticket #58
#from manager.apps.brand.views import OwnerListView, OwnerView
from manager.apps.brand.views import BrandProposalView

urlpatterns = patterns(
    '',
    url(r'^brand/$', BrandListView.as_view(), name='brandlist'),
    url(r'^brand/(?P<bsin>[1-9A-NP-Z]{6})', BrandView.as_view(), name='brand'),
    url(r'^brand/new/$', BrandProposalView.as_view(), name='brandproposal'),
    url(r'^brand/proposed/$', TemplateView.as_view(
        template_name='brand/brandproposed.jade'), name='brandproposed'),

    # Postponed in ticket #58
    #url(r'^owner/$', OwnerListView.as_view(), name='ownerlist'),
    #url(r'^owner/(?P<cd>[1-9]+)', OwnerView.as_view(), name='owner'),
)
