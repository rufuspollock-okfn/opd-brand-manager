from django.contrib import admin
from django.db import models
from django.conf.urls import patterns
from django.http import HttpResponse
from .models import Brand, BrandType, BrandProposal, BrandProposalReview \
    # [#58] , BrandOwner
from .widget import AdminImageWidget
from .filters import ReviewedFilter
from .forms import ProposalReviewForm


class BrandTypeAdmin(admin.ModelAdmin):
    actions = None

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(BrandType, BrandTypeAdmin)

# Postponed in ticket #58
#class BrandOwnerAdmin(admin.ModelAdmin):
#    actions = None
#    list_display = ('owner_nm', 'owner_logo_admin', 'owner_link')
#    fields = (
#        'owner_nm', 'owner_link', 'owner_logo')
#    search_fields = ['owner_nm']
#
#    # Never delete a brand, update its BSIN
#    def has_delete_permission(self, request, obj=None):
#        return False

#admin.site.register(BrandOwner, BrandOwnerAdmin)


class BrandAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('bsin', 'brand_nm', 'brand_logo_admin', 'flag_delete')
    fields_add = (
        (None, {
            'classes': ('wide',),
            'fields': ('bsin', 'brand_nm',
                       # Postponed in ticket #58
                       #'owner_cd',
                       'brand_type_cd', 'brand_link', 'brand_logo',
                       'comments', 'last_modified')
        }),
    )
    fields_change = (
        (None, {
            'classes': ('wide',),
            'fields': ('bsin', 'brand_nm',
                       # Postponed in ticket #58
                       #'owner_cd',
                       'brand_type_cd', 'brand_link', 'brand_logo',
                       ('flag_delete', 'comments'),
                       'last_modified')
        }),
    )
    readonly_fields_su = ('bsin', 'last_modified')
    readonly_fields_moderator = ('bsin', 'last_modified', 'brand_nm')
    search_fields = ['bsin', 'brand_nm',
                     # Postponed in ticket #58
                     #'owner_cd__owner_nm'
                     ]
    list_filter = ('flag_delete', )
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

    def get_fieldsets(self, request, obj=None):
        # if editing
        if obj:
            return self.fields_change
        return self.fields_add

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields_su
        return self.readonly_fields_moderator

admin.site.register(Brand, BrandAdmin)


class BrandProposalAdmin(admin.ModelAdmin):
    form = ProposalReviewForm
    actions = None
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }
    readonly_fields_modify = ('brand_nm', 'brand_type_cd', 'brand_link',
                              'user', 'status', 'comments', 'brand_logo')
    readonly_fields_create = ('user', 'status', 'comments')
    list_display = ('brand_nm', 'user')
    list_filter = (ReviewedFilter, )

    def save_model(self, request, obj, form, change):
        bpr, created = BrandProposalReview.objects.get_or_create(
            proposal_cd_id=obj.proposal_cd, user=request.user)
        bpr.comments = form.data['moderator_comment']
        bpr.save()
        obj.save()

    def get_object(self, request, object_id):
        obj = super(BrandProposalAdmin, self).get_object(request, object_id)

        try:
            bpr = BrandProposalReview.objects.get(
                user=request.user, proposal_cd=object_id)
            obj.moderator_comment = bpr.comments
        except BrandProposalReview.DoesNotExist:
            pass

        return obj

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if BrandProposalReview.objects.filter(
                    proposal_cd=obj.proposal_cd,
                    user=request.user).count() > 0:
                return self.readonly_fields_modify
        return self.readonly_fields_create

    def get_urls(self):
        urls = super(BrandProposalAdmin, self).get_urls()
        bp_urls = patterns(
            '', (r'^review/$', self.admin_site.admin_view(self.view)))
        return bp_urls + urls

    def view(self, request):
        # custom view which should return an HttpResponse
        return HttpResponse('Test')

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('field_to_hide')
        return super(BrandProposalAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(BrandProposal, BrandProposalAdmin)


class BrandProposalReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('proposal_cd', 'user')

    def has_add_permission(self, request):
        return False

    def queryset(self, request):
        qs = super(BrandProposalReviewAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(user=request.user)

admin.site.register(BrandProposalReview, BrandProposalReviewAdmin)
