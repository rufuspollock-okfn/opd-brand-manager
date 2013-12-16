from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from manager.libs.snippets.username import generate_random_username
from .models import Brand, BrandProposal  # [#58] , BrandOwner
from .forms import BrandProposalForm
from django.core.urlresolvers import reverse


# Postponed in ticket #58
# class OwnerListView(View):
#     r"""
#     Owner list.
#     """

#     template_name = 'brand/ownerlist.jade'

#     def get(self, request):
#         search = request.GET.get('search', '')
#         if search != '':
#             owner_list = BrandOwner.objects.filter(
#                 owner_nm__icontains=search)
#         else:
#             owner_list = BrandOwner.objects.all()
#         paginator = Paginator(owner_list, 25)  # Show 25 owners per page

#         page = request.GET.get('page')
#         try:
#             owners = paginator.page(page)
#         except PageNotAnInteger:
#             # If page is not an integer, deliver first page.
#             owners = paginator.page(1)
#         except EmptyPage:
#             # If page is out of range, deliver last page of results.
#             owners = paginator.page(paginator.num_pages)
#         return render(request, self.template_name, {
#                       'owners': owners,
#                       'search': search})

# Postponed in ticket #58
# class OwnerView(View):
#     r"""
#     Owner details.
#     """

#     template_name = 'brand/owner.jade'

#     def get(self, request, cd):
#         try:
#             owner = BrandOwner.objects.get(owner_cd__iexact=cd)
#         except ObjectDoesNotExist:
#             return HttpResponseNotFound('<h1>Owner not found</h1>')
#         return render(request, self.template_name, {
#                       'owner': owner})


class BrandListView(View):
    r"""
    Brand list.
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
    Brand details.
    """

    template_name = 'brand/brand.jade'

    def get(self, request, bsin):
        try:
            brand = Brand.objects.get(bsin=bsin)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1>Brand not found</h1>')
        return render(request, self.template_name, {
                      'brand': brand,
                      # Postponed in ticket #58
                      #'owner': brand.owner_cd
                      })


class BrandProposalView(FormView):
    r"""
    View to allow guests to propose a brand.
    """

    template_name = 'brand/brandproposalplaceholder.jade'
    form_class = BrandProposalForm

    def get_success_url(self):
        return reverse('brandproposed')

    def get(self, request):
        form = BrandProposalForm()  # An unbound form

        return render(request, self.template_name, {
                      'form': form})

    def form_valid(self, form):
        user, created = User.objects.get_or_create(
            email=form.cleaned_data['sender'],
            defaults={
                'username': generate_random_username(),
                'is_staff': False,
                'is_active': False,
                'is_superuser': False})
        if created:
            user.save()
        proposal = BrandProposal(
            brand_nm=form.cleaned_data['brand_nm'],
            # Postponed in ticket #58
            #owner_nm=form.cleaned_data['owner_nm'],
            brand_link=form.cleaned_data['brand_link'],
            brand_type_cd=form.cleaned_data['brand_type'],
            comments=form.cleaned_data['comments'],
            user=user,
            #save the logo after the proposal is created in the DB
            #because upload_to requires the primary key to be set
            brand_logo=form.cleaned_data['brand_logo'])
        proposal.save()

        return super(BrandProposalView, self).form_valid(form)
