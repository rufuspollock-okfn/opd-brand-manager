# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table(u'brand', (
            ('bsin', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True, db_column=u'BSIN')),
            ('brand_nm', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'BRAND_NM')),
            ('group_cd', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'GROUP_CD', blank=True)),
            ('brand_type_cd', self.gf('django.db.models.fields.IntegerField')(db_column=u'BRAND_TYPE_CD')),
            ('brand_link', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'BRAND_LINK', blank=True)),
            ('crea_dt', self.gf('django.db.models.fields.DateTimeField')(db_column=u'CREA_DT')),
            ('modif_dt', self.gf('django.db.models.fields.DateTimeField')(db_column=u'MODIF_DT')),
            ('suppr_dt', self.gf('django.db.models.fields.DateTimeField')(db_column=u'SUPPR_DT')),
            ('suppr_flag', self.gf('django.db.models.fields.IntegerField')(db_column=u'SUPPR_FLAG')),
        ))
        db.send_create_signal(u'brand', ['Brand'])

        # Adding model 'BrandGroup'
        db.create_table(u'brand_group', (
            ('group_cd', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'GROUP_CD')),
            ('group_nm', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'GROUP_NM')),
            ('group_link', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'GROUP_LINK')),
            ('group_wiki_en', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'GROUP_WIKI_EN')),
        ))
        db.send_create_signal(u'brand', ['BrandGroup'])

        # Adding model 'BrandType'
        db.create_table(u'brand_type', (
            ('brand_type_cd', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'BRAND_TYPE_CD')),
            ('brand_type_nm', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'BRAND_TYPE_NM')),
        ))
        db.send_create_signal(u'brand', ['BrandType'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table(u'brand')

        # Deleting model 'BrandGroup'
        db.delete_table(u'brand_group')

        # Deleting model 'BrandType'
        db.delete_table(u'brand_type')


    models = {
        u'brand.brand': {
            'Meta': {'object_name': 'Brand', 'db_table': "u'brand'"},
            'brand_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_LINK'", 'blank': 'True'}),
            'brand_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_NM'"}),
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'db_column': "u'BRAND_TYPE_CD'"}),
            'bsin': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'BSIN'"}),
            'crea_dt': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'CREA_DT'"}),
            'group_cd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'GROUP_CD'", 'blank': 'True'}),
            'modif_dt': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'MODIF_DT'"}),
            'suppr_dt': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'SUPPR_DT'"}),
            'suppr_flag': ('django.db.models.fields.IntegerField', [], {'db_column': "u'SUPPR_FLAG'"})
        },
        u'brand.brandgroup': {
            'Meta': {'object_name': 'BrandGroup', 'db_table': "u'brand_group'"},
            'group_cd': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'GROUP_CD'"}),
            'group_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'GROUP_LINK'"}),
            'group_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'GROUP_NM'"}),
            'group_wiki_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'GROUP_WIKI_EN'"})
        },
        u'brand.brandtype': {
            'Meta': {'object_name': 'BrandType', 'db_table': "u'brand_type'"},
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'BRAND_TYPE_CD'"}),
            'brand_type_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_TYPE_NM'"})
        }
    }

    complete_apps = ['brand']