from django.contrib import admin
from django import forms
from .models import Brand, BrandOwner, BrandType


class BrandTypeAdmin(admin.ModelAdmin):
    actions = None

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(BrandType, BrandTypeAdmin)


class BrandOwnerAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('owner_nm', 'owner_link')
    fields = (
        'owner_nm', 'owner_link', 'owner_wiki_en')
    search_fields = ['owner_nm']

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(BrandOwner, BrandOwnerAdmin)


class BrandAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('bsin', 'brand_nm', 'brand_logo_admin', 'flag_delete')
    fields = (
        'bsin', 'brand_nm', 'owner_cd', 'brand_type_cd', 'brand_link',
        'brand_logo', ('flag_delete', 'comments'), 'last_modified')
    readonly_fields = ('bsin', 'last_modified')
    search_fields = ['bsin', 'brand_nm', 'owner_cd__owner_nm']
    list_filter = ('flag_delete', )

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Brand, BrandAdmin)
