"""
Auto-generated models from Philippe Plagnol architecture for brand, brand owner
and brand type base on SQL file
/database/brand_2013.11.13_01.sql

For more information about auto-generating models, see
https://docs.djangoproject.com/fr/1.6/howto/legacy-databases/
"""

from __future__ import unicode_literals
from django.db import models
from manager.libs.snippets.bsin import BSIN
from django.core.validators import RegexValidator
from django.templatetags.static import static
import os


def get_brand_logo_path(instance, filename):
    return os.path.join('brand', 'logo', '%s.jpg' % instance.bsin)

class Brand(models.Model):
    """
    Brand.
    """

    bsin = models.CharField(db_column='BSIN', primary_key=True, max_length=6,
        verbose_name='BSIN', validators=[BSIN.BSINValidator])
    brand_nm = models.CharField(db_column='BRAND_NM', max_length=255,
        verbose_name='Brand name')
    owner_cd = models.ForeignKey(
        'BrandOwner', db_column='OWNER_CD', blank=True, null=True,
        verbose_name='Owner')
    brand_type_cd = models.ForeignKey('BrandType', db_column='BRAND_TYPE_CD',
        verbose_name='Brand type')
    brand_link = models.URLField(
        db_column='BRAND_LINK', max_length=255, blank=True, null=True,
        verbose_name='Brand link')
    brand_logo = models.ImageField(
        db_column='BRAND_LOGO', verbose_name='Brand logo',
        upload_to=get_brand_logo_path, blank=True, null=True)
    flag_delete = models.BooleanField(db_column='FLAG_DELETE', default=False,
        verbose_name='Deleted flag')
    last_modified = models.DateTimeField(
        db_column='LAST_MODIFIED', auto_now=True,
        verbose_name='Last modified')
    comments = models.CharField(
        db_column='COMMENTS', max_length=255, blank=True, null=True,
        verbose_name='Comments')

    flag_delete.admin_order_field = 'flag_delete'
    flag_delete.boolean = False
    flag_delete.short_description = 'Brand is deleted?'

    def brand_logo_admin(self):
        if self.brand_logo:
            return '<img width="32" height"32" src="%s"/>' % (
                self.brand_logo.url)
        else:
            return '<img width="32" height"32" src="%s" />' % (
                static('brand/images/no_picture.gif'))

    brand_logo_admin.allow_tags = True

    class Meta:
        db_table = 'brand'
        unique_together = ('brand_nm', 'owner_cd')
        ordering = ['brand_nm']

    def __unicode__(self):
        return self.brand_nm

    @classmethod
    def get_available_bsin(cls):
        """
        Generates an available BSIN.
        """
        bsin = BSIN.generate_BSIN()
        while not cls.is_available_bsin(bsin):
            bsin = BSIN.generate_BSIN()

        return bsin

    @classmethod
    def is_available_bsin(cls, bsin):
        """
        Check if BSIN availability and return a boolean.
        """
        try:
            self.objects.get(bsin=bsin)
            return False
        except Brand.DoesNotExist:
            return True

    def save(self, *args, **kwargs):
        super(Brand, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Never delete a brand.
        """
        pass


class BrandOwner(models.Model):
    """
    Legal owner of the brand.
    """

    owner_cd = models.IntegerField(db_column='OWNER_CD', primary_key=True)
    owner_nm = models.CharField(db_column='OWNER_NM', max_length=255)
    owner_link = models.CharField(db_column='OWNER_LINK', max_length=255)
    owner_wiki_en = models.CharField(db_column='OWNER_WIKI_EN', max_length=255)

    class Meta:
        db_table = 'brand_owner'

    def __unicode__(self):
        return self.owner_nm
        ordering = ['owner_nm']


class BrandType(models.Model):
    """
    Brand owner by manufacturer and retailers are of 2 different types. The
    repository contains groups of brands when the number of brand is too
    important and that the number of product is small (Wine, Cheese,...).
    """

    brand_type_cd = models.IntegerField(
        db_column='BRAND_TYPE_CD', primary_key=True)
    brand_type_nm = models.CharField(db_column='BRAND_TYPE_NM', max_length=255)

    class Meta:
        db_table = 'brand_type'

    def __unicode__(self):
        return self.brand_type_nm
