from django.contrib import admin
from django import forms
from .models import Brand, BrandOwner, BrandType

admin.site.register(BrandOwner)
admin.site.register(BrandType)


class BrandAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('bsin', 'brand_nm', 'brand_logo_admin', 'flag_delete')
    fields = (
        'bsin', 'brand_nm', 'owner_cd', 'brand_type_cd', 'brand_link',
        ('flag_delete', 'comments'), 'last_modified')
    readonly_fields = ('bsin', 'last_modified')

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Brand, BrandAdmin)
