from tastypie.resources import ModelResource
from manager.apps.brand.models import Brand, BrandOwner


class BrandResource(ModelResource):
    class Meta:
        queryset = Brand.objects.filter(flag_delete=False)
        resource_name = 'brand'
        allowed_methods = ['get']


class BrandOwnerResource(ModelResource):
    class Meta:
        queryset = BrandOwner.objects.all()
        resource_name = 'brand_owner'
        allowed_methods = ['get']
