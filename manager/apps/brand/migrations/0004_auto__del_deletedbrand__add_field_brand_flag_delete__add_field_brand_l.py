# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DeletedBrand'
        db.delete_table(u'deleted_brand')

        # Adding field 'Brand.flag_delete'
        db.add_column(u'brand', 'flag_delete',
                      self.gf('django.db.models.fields.BooleanField')(default=False, db_column=u'FLAG_DELETE'),
                      keep_default=False)

        # Adding field 'Brand.last_modified'
        db.add_column(u'brand', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime.now(), db_column=u'LAST_MODIFIED', blank=True),
                      keep_default=False)

        # Adding field 'Brand.comments'
        db.add_column(u'brand', 'comments',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, db_column=u'COMMENTS', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'DeletedBrand'
        db.create_table(u'deleted_brand', (
            ('bsin', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True, db_column=u'BSIN')),
            ('brand_nm', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'BRAND_NM')),
            ('brand_link', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'BRAND_LINK', blank=True)),
            ('brand_type_cd', self.gf('django.db.models.fields.IntegerField')(db_column=u'BRAND_TYPE_CD')),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'REASON')),
            ('owner_cd', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'OWNER_CD', blank=True)),
        ))
        db.send_create_signal(u'brand', ['DeletedBrand'])

        # Deleting field 'Brand.flag_delete'
        db.delete_column(u'brand', u'FLAG_DELETE')

        # Deleting field 'Brand.last_modified'
        db.delete_column(u'brand', u'LAST_MODIFIED')

        # Deleting field 'Brand.comments'
        db.delete_column(u'brand', u'COMMENTS')


    models = {
        u'brand.brand': {
            'Meta': {'object_name': 'Brand', 'db_table': "u'brand'"},
            'brand_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_LINK'", 'blank': 'True'}),
            'brand_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_NM'"}),
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'db_column': "u'BRAND_TYPE_CD'"}),
            'bsin': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'BSIN'"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_column': "u'COMMENTS'", 'blank': 'True'}),
            'flag_delete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'FLAG_DELETE'"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "u'LAST_MODIFIED'", 'blank': 'True'}),
            'owner_cd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'OWNER_CD'", 'blank': 'True'})
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