from django.shortcuts import render
from django.views.generic import View
from .models import Brand, BrandOwner
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound


class OwnerListView(View):
    r"""
    """

    template_name = 'brand/ownerlist.jade'

    def get(self, request):
        search = request.GET.get('search', '')
        if search != '':
            owner_list = BrandOwner.objects.filter(owner_nm__icontains=search)
        else:
            owner_list = BrandOwner.objects.all()
        paginator = Paginator(owner_list, 25)  # Show 25 owners per page

        page = request.GET.get('page')
        try:
            owners = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            owners = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            owners = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {
                      'owners': owners,
                      'search': search})


class OwnerView(View):
    r"""
    """

    template_name = 'brand/owner.jade'

    def get(self, request, cd):
        try:
            owner = BrandOwner.objects.get(owner_cd__iexact=cd)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1>Owner not found</h1>')
        return render(request, self.template_name, {
                      'owner': owner})


class BrandListView(View):
    r"""
    """

    template_name = 'brand/brandlist.jade'

    def get(self, request):
        search = request.GET.get('search', '')
        if search != '':
            brand_list = Brand.objects.filter(brand_nm__icontains=search)
            brand_list = filter(lambda brand: not brand.flag_delete,
                                brand_list)
        else:
            brand_list = Brand.objects.filter(flag_delete=False)
        paginator = Paginator(brand_list, 25)  # Show 25 brands per page

        page = request.GET.get('page')
        try:
            brands = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            brands = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            brands = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {
                      'brands': brands,
                      'search': search})


class BrandView(View):
    r"""
    """

    template_name = 'brand/brand.jade'

    def get(self, request, bsin):
        try:
            brand = Brand.objects.get(bsin=bsin)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1>Brand not found</h1>')
        return render(request, self.template_name, {
                      'brand': brand,
                      'owner': brand.owner_cd})
