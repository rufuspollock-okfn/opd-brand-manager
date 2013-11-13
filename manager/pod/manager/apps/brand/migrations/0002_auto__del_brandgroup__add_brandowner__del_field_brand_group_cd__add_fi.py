# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming model 'BrandGroup' into 'BrandOwner'
        db.rename_table(u'brand_group', u'brand_owner')

        # Renaming 'group_cd' field to 'owner_cd'
        db.rename_column('brand_owner', 'GROUP_CD', 'OWNER_CD')

        # Renaming 'group_nm' field to 'owner_nm'
        db.rename_column('brand_owner', 'GROUP_NM', 'OWNER_NM')

        # Renaming 'group_link' field to 'owner_link'
        db.rename_column('brand_owner', 'GROUP_LINK', 'OWNER_LINK')

        # Renaming 'group_wiki_en' field to 'owner_wiki_en'
        db.rename_column('brand_owner', 'GROUP_WIKI_EN', 'OWNER_WIKI_EN')

        # Deleting field 'Brand.group_cd'
        db.rename_column('brand', 'GROUP_CD', 'OWNER_CD')

        # Adding the corresponding foreign key
        db.alter_column('brand', 'OWNER_CD',
            models.ForeignKey(
                orm['brand.BrandOwner'],
                blank=True,
                null=True,
            )
        )

    def backwards(self, orm):

        # No backward compatibility
        raise RuntimeError("No backwards.")

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
