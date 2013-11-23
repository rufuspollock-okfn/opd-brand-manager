from django.conf.urls import patterns, url
from manager.apps.brand.views import BrandView

urlpatterns = patterns(
    '',
    url(r'^$', BrandView.as_view(), name='brandlist'),
)
