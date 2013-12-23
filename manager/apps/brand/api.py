from tastypie.resources import ModelResource
from manager.apps.brand.models import Brand  # [#58] , BrandOwner
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from haystack.query import SearchQuerySet
from tastypie.utils import trailing_slash
from django.conf.urls import url


class BrandResource(ModelResource):
    class Meta:
        queryset = Brand.objects.filter(flag_delete=False)
        resource_name = 'brand'
        allowed_methods = ['get']

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (
                self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_search'), name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        # Do the query.
        query = request.GET.get('q', '')
        sqs = SearchQuerySet().models(Brand).filter(brand_nm__startswith=query)
        paginator = Paginator(sqs, 20)

        try:
            page = paginator.page(int(request.GET.get('page', 1)))
        except InvalidPage:
            raise Http404("Sorry, no results on that page.")

        objects = []

        for result in page.object_list:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)


# Postponed in ticket #58
#class BrandOwnerResource(ModelResource):
#    class Meta:
#        queryset = BrandOwner.objects.all()
#        resource_name = 'brand_owner'
#        allowed_methods = ['get']
