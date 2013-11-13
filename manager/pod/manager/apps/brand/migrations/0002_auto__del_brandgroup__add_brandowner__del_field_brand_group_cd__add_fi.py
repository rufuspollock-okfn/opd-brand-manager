# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BrandGroup'
        db.delete_table(u'brand_group')

        # Adding model 'BrandOwner'
        db.create_table(u'brand_owner', (
            ('owner_cd', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'OWNER_CD')),
            ('owner_nm', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'OWNER_NM')),
            ('owner_link', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'OWNER_LINK')),
            ('owner_wiki_en', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'OWNER_WIKI_EN')),
        ))
        db.send_create_signal(u'brand', ['BrandOwner'])

        # Deleting field 'Brand.group_cd'
        db.delete_column(u'brand', u'GROUP_CD')

        # Adding field 'Brand.owner_cd'
        db.add_column(u'brand', 'owner_cd',
                      self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'OWNER_CD', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'BrandGroup'
        db.create_table(u'brand_group', (
            ('group_nm', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'GROUP_NM')),
            ('group_cd', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'GROUP_CD')),
            ('group_wiki_en', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'GROUP_WIKI_EN')),
            ('group_link', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'GROUP_LINK')),
        ))
        db.send_create_signal(u'brand', ['BrandGroup'])

        # Deleting model 'BrandOwner'
        db.delete_table(u'brand_owner')

        # Adding field 'Brand.group_cd'
        db.add_column(u'brand', 'group_cd',
                      self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'GROUP_CD', blank=True),
                      keep_default=False)

        # Deleting field 'Brand.owner_cd'
        db.delete_column(u'brand', u'OWNER_CD')


    models = {
        u'brand.brand': {
            'Meta': {'object_name': 'Brand', 'db_table': "u'brand'"},
            'brand_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_LINK'", 'blank': 'True'}),
            'brand_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_NM'"}),
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'db_column': "u'BRAND_TYPE_CD'"}),
            'bsin': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'BSIN'"}),
            'crea_dt': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'CREA_DT'"}),
            'modif_dt': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'MODIF_DT'"}),
            'owner_cd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'OWNER_CD'", 'blank': 'True'}),
            'suppr_dt': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'SUPPR_DT'"}),
            'suppr_flag': ('django.db.models.fields.IntegerField', [], {'db_column': "u'SUPPR_FLAG'"})
        },
        u'brand.brandowner': {
            'Meta': {'object_name': 'BrandOwner', 'db_table': "u'brand_owner'"},
            'owner_cd': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'OWNER_CD'"}),
            'owner_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'OWNER_LINK'"}),
            'owner_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'OWNER_NM'"}),
            'owner_wiki_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'OWNER_WIKI_EN'"})
        },
        u'brand.brandtype': {
            'Meta': {'object_name': 'BrandType', 'db_table': "u'brand_type'"},
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'BRAND_TYPE_CD'"}),
            'brand_type_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_TYPE_NM'"})
        }
    }

    complete_apps = ['brand']