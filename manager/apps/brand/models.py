"""
Auto-generated models from Philippe Plagnol architecture for brand, brand owner
and brand type base on SQL file
/database/brand_2013.11.13_01.sql

For more information about auto-generating models, see
https://docs.djangoproject.com/fr/1.6/howto/legacy-databases/
"""

from __future__ import unicode_literals
from django.db import models


class Brand(models.Model):
    bsin = models.CharField(db_column='BSIN', primary_key=True, max_length=6)
    brand_nm = models.CharField(db_column='BRAND_NM', max_length=255)
    owner_cd = models.IntegerField(db_column='OWNER_CD', blank=True, null=True)
    brand_type_cd = models.IntegerField(db_column='BRAND_TYPE_CD')
    brand_link = models.CharField(db_column='BRAND_LINK', max_length=255,
        blank=True)
    flag_delete = models.BooleanField(db_column='FLAG_DELETE', default=False)
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED',
        auto_now=True)
    comments = models.CharField(db_column='COMMENTS', max_length=255,
        blank=True, null=True)

    class Meta:
        db_table = 'brand'

    def __unicode__(self):
        return self.brand_nm


class BrandOwner(models.Model):
    owner_cd = models.IntegerField(db_column='OWNER_CD', primary_key=True)
    owner_nm = models.CharField(db_column='OWNER_NM', max_length=255)
    owner_link = models.CharField(db_column='OWNER_LINK', max_length=255)
    owner_wiki_en = models.CharField(db_column='OWNER_WIKI_EN', max_length=255)

    class Meta:
        db_table = 'brand_owner'

    def __unicode__(self):
        return self.owner_nm


class BrandType(models.Model):
    brand_type_cd = models.IntegerField(db_column='BRAND_TYPE_CD',
        primary_key=True)
    brand_type_nm = models.CharField(db_column='BRAND_TYPE_NM', max_length=255)

    class Meta:
        db_table = 'brand_type'

    def __unicode__(self):
        return self.brand_type_nm
