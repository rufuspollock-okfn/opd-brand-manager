from django.contrib import admin
from .models import Brand, BrandOwner, BrandType

admin.site.register(Brand)
admin.site.register(BrandOwner)
admin.site.register(BrandType)
