from django.shortcuts import render
from django.views.generic import View
from .models import Brand, BrandOwner, BrandType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound


class BrandListView(View):
    r"""
    """

    template_name = 'main/brandlist.jade'
    allBrands = Brand.objects.all()

    def get(self, request):
        brand_list = Brand.objects.filter(flag_delete=False)
        paginator = Paginator(brand_list, 25) # Show 100 brands per page

        page = request.GET.get('page')
        try:
            brands = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            brands = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            brands = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {'brands': brands})


class BrandView(View):
    r"""
    """

    template_name = 'main/brand.jade'

    def get(self, request, bsin):
        try:
            brand = Brand.objects.get(bsin=bsin)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1>Brand not found</h1>')
        return render(request, self.template_name, {
        'brand': brand,
        'owner': brand.owner_cd})
