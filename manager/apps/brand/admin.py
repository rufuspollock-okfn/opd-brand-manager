from django.contrib import admin
from django.forms import ModelForm
from .models import Brand, BrandOwner, BrandType

admin.site.register(BrandOwner)
admin.site.register(BrandType)


class BrandForm(ModelForm):

    class Meta:
        model = Brand
        exclude = ['bsin', 'last_modified']


class BrandAdmin(admin.ModelAdmin):
    actions = None
    form = BrandForm
    fields = (
        'bsin', 'brand_nm', 'owner_cd', 'brand_type_cd', 'brand_link',
        ('flag_delete', 'comments'), 'last_modified')
    readonly_fields = ('bsin', 'last_modified')

    # Never delete a brand, update its BSIN
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Brand, BrandAdmin)
