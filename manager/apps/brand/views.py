from django.shortcuts import render
from django.views.generic import View
from .models import Brand, BrandOwner, BrandType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BrandView(View):
    r"""
    """

    template_name = 'main/brandlist.jade'
    allBrands = Brand.objects.all()

    def get(self, request):
        brand_list = Brand.objects.all()
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
