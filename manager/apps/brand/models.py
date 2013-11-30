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
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.templatetags.static import static
from django.contrib.auth.models import User
import os


def get_brand_logo_path(instance, filename):
    return os.path.join('brand', 'logo', '%s.jpg' % instance.bsin)


class SoftDeletionQuerySet(models.query.QuerySet):
    """
    Custom queryset to avoid bulk delete.
    """

    def delete(self):
        pass


class SoftDeletionManager(models.Manager):
    """
    Custom manager to avoid bulk delete.
    """

    def __init__(self, *args, **kwargs):
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        return SoftDeletionQuerySet(self.model)


class Brand(models.Model):
    """
    Brand.
    """

    bsin = models.CharField(
        db_column='BSIN', primary_key=True, max_length=6,
        verbose_name='BSIN', validators=[BSIN.BSINValidator])
    brand_nm = models.CharField(
        db_column='BRAND_NM', max_length=255, verbose_name='Brand name')
    owner_cd = models.ForeignKey(
        'BrandOwner', db_column='OWNER_CD', blank=True, null=True,
        verbose_name='Owner')
    brand_type_cd = models.ForeignKey(
        'BrandType', db_column='BRAND_TYPE_CD', verbose_name='Brand type')
    brand_link = models.URLField(
        db_column='BRAND_LINK', max_length=255, blank=True, null=True,
        verbose_name='Brand link')
    brand_logo = models.ImageField(
        db_column='BRAND_LOGO', verbose_name='Brand logo',
        upload_to=get_brand_logo_path, blank=True, null=True)
    flag_delete = models.BooleanField(
        db_column='FLAG_DELETE', default=False, verbose_name='Deleted flag',
        editable=False)
    last_modified = models.DateTimeField(
        db_column='LAST_MODIFIED', auto_now=True,
        verbose_name='Last modified')
    comments = models.TextField(
        db_column='COMMENTS', validators=[MaxLengthValidator(255)], blank=True,
        null=True, verbose_name='Comments')

    objects = SoftDeletionManager()

    # Flag delete
    flag_delete.admin_order_field = 'flag_delete'
    flag_delete.boolean = False
    flag_delete.short_description = 'Brand is deleted?'

    # Brand logo
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
            cls.objects.get(bsin=bsin)
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


def get_owner_logo_path(instance, filename):
    return os.path.join('owner', 'logo', '%06d.jpg' % instance.owner_cd)


class BrandOwner(models.Model):
    """
    Legal owner of the brand.
    """

    owner_cd = models.IntegerField(db_column='OWNER_CD', primary_key=True)
    owner_nm = models.CharField(
        db_column='OWNER_NM', max_length=255, verbose_name='Owner name')
    owner_logo = models.ImageField(
        db_column='OWNER_LOGO', verbose_name='Owner logo',
        upload_to=get_owner_logo_path, blank=True, null=True)
    owner_link = models.URLField(
        db_column='OWNER_LINK', max_length=255, null=True, blank=True,
        verbose_name='Owner website')
    owner_wiki_en = models.URLField(
        db_column='OWNER_WIKI_EN', max_length=255, null=True, blank=True,
        verbose_name='Wikipedia English website')

    objects = SoftDeletionManager()

    class Meta:
        db_table = 'brand_owner'
        ordering = ['owner_nm']

    def __unicode__(self):
        return self.owner_nm

    def owner_logo_admin(self):
        if self.owner_logo:
            return '<img width="32" height"32" src="%s"/>' % (
                self.owner_logo.url)
        else:
            return '<img width="32" height"32" src="%s" />' % (
                static('brand/images/no_picture.gif'))

    owner_logo_admin.allow_tags = True

    def delete(self, *args, **kwargs):
        """
        Never delete an owner.
        """

        pass


class BrandType(models.Model):
    """
    Brand owner by manufacturer and retailers are of 2 different types. The
    repository contains groups of brands when the number of brand is too
    important and that the number of product is small (Wine, Cheese,...).
    """

    brand_type_cd = models.IntegerField(
        db_column='BRAND_TYPE_CD', primary_key=True)
    brand_type_nm = models.CharField(db_column='BRAND_TYPE_NM', max_length=255)

    objects = SoftDeletionManager()

    class Meta:
        db_table = 'brand_type'

    def __unicode__(self):
        return self.brand_type_nm

    def delete(self, *args, **kwargs):
        """
        Never delete a type.
        """

        pass


def get_brand_proposal_logo_path(instance, filename):
    return os.path.join('brandproposal',
                        'logo',
                        '%s.jpg' % instance.proposal_cd)


class BrandProposal(models.Model):
    """
    BrandProposal. Anyone can create a proposal, but it can only be
    transformed into a real Brand with a bsin by a moderator
    or an administrator
    """

    proposal_cd = models.AutoField(
        db_column='PROPOSAL_CD', primary_key=True)
    brand_nm = models.CharField(
        db_column='BRAND_NM', max_length=255, verbose_name='Brand name')
    brand_type_cd = models.ForeignKey(
        'BrandType', db_column='BRAND_TYPE_CD', verbose_name='Brand type')
    owner_nm = models.CharField(
        db_column='OWNER_NM', max_length=255, verbose_name='Owner name')
    brand_link = models.URLField(
        db_column='BRAND_LINK', max_length=255, blank=True, null=True,
        verbose_name='Brand link')
    brand_logo = models.ImageField(
        db_column='BRAND_LOGO', verbose_name='Brand logo',
        upload_to=get_brand_proposal_logo_path, blank=True, null=True)
    insert_date = models.DateTimeField(
        db_column='INSERT_DATE', auto_now_add=True,
        verbose_name='Insert date')
    comments = models.TextField(
        db_column='COMMENTS', validators=[MaxLengthValidator(255)], blank=True,
        null=True, verbose_name='Comments')
    status = models.IntegerField(
        db_column='STATUS',
        validators=[MinValueValidator(1), MaxValueValidator(4)],
        default=1, verbose_name='Status')
    user = models.ForeignKey(
        User, db_column='USER_ID',
        verbose_name='User')

    def brand_logo_admin(self):
        if self.brand_logo:
            return '<img width="32" height"32" src="%s"/>' % (
                self.brand_logo.url)
        else:
            return '<img width="32" height"32" src="%s" />' % (
                static('brand/images/no_picture.gif'))

    brand_logo_admin.allow_tags = True

    class Meta:
        db_table = 'brand_proposal'
        ordering = ['insert_date']

    def __unicode__(self):
        return self.brand_nm
