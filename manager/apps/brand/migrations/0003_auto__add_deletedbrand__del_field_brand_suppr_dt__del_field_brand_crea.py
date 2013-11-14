# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeletedBrand'
        db.create_table(u'deleted_brand', (
            ('bsin', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True, db_column=u'BSIN')),
            ('brand_nm', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'BRAND_NM')),
            ('owner_cd', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'OWNER_CD', blank=True)),
            ('brand_type_cd', self.gf('django.db.models.fields.IntegerField')(db_column=u'BRAND_TYPE_CD')),
            ('brand_link', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'BRAND_LINK', blank=True)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'REASON')),
        ))
        db.send_create_signal(u'brand', ['DeletedBrand'])

        # Deleting field 'Brand.suppr_dt'
        db.delete_column(u'brand', u'SUPPR_DT')

        # Deleting field 'Brand.crea_dt'
        db.delete_column(u'brand', u'CREA_DT')

        # Deleting field 'Brand.suppr_flag'
        db.delete_column(u'brand', u'SUPPR_FLAG')

        # Deleting field 'Brand.modif_dt'
        db.delete_column(u'brand', u'MODIF_DT')


    def backwards(self, orm):
        # Deleting model 'DeletedBrand'
        db.delete_table(u'deleted_brand')


        # User chose to not deal with backwards NULL issues for 'Brand.suppr_dt'
        raise RuntimeError("Cannot reverse this migration. 'Brand.suppr_dt' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Brand.suppr_dt'
        db.add_column(u'brand', 'suppr_dt',
                      self.gf('django.db.models.fields.DateTimeField')(db_column=u'SUPPR_DT'),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Brand.crea_dt'
        raise RuntimeError("Cannot reverse this migration. 'Brand.crea_dt' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Brand.crea_dt'
        db.add_column(u'brand', 'crea_dt',
                      self.gf('django.db.models.fields.DateTimeField')(db_column=u'CREA_DT'),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Brand.suppr_flag'
        raise RuntimeError("Cannot reverse this migration. 'Brand.suppr_flag' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Brand.suppr_flag'
        db.add_column(u'brand', 'suppr_flag',
                      self.gf('django.db.models.fields.IntegerField')(db_column=u'SUPPR_FLAG'),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Brand.modif_dt'
        raise RuntimeError("Cannot reverse this migration. 'Brand.modif_dt' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Brand.modif_dt'
        db.add_column(u'brand', 'modif_dt',
                      self.gf('django.db.models.fields.DateTimeField')(db_column=u'MODIF_DT'),
                      keep_default=False)


    models = {
        u'brand.brand': {
            'Meta': {'object_name': 'Brand', 'db_table': "u'brand'"},
            'brand_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_LINK'", 'blank': 'True'}),
            'brand_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_NM'"}),
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'db_column': "u'BRAND_TYPE_CD'"}),
            'bsin': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'BSIN'"}),
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
        },
        u'brand.deletedbrand': {
            'Meta': {'object_name': 'DeletedBrand', 'db_table': "u'deleted_brand'"},
            'brand_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_LINK'", 'blank': 'True'}),
            'brand_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_NM'"}),
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'db_column': "u'BRAND_TYPE_CD'"}),
            'bsin': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'BSIN'"}),
            'owner_cd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'OWNER_CD'", 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'REASON'"})
        }
    }

    complete_apps = ['brand']