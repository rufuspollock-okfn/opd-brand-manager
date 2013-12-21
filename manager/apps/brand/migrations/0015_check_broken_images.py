# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from manager.libs.snippets.http_tools import http_destination_exists
from django.conf import settings
import urlparse


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass

        # Postponed in ticket #58
        #from manager.apps.brand.models import BrandOwner

        ## Updating brand url field to append default http protocol
        #db.execute("UPDATE BRAND_OWNER SET \"OWNER_LOGO\"=CONCAT(CONCAT('owner/logo/', lpad(\"OWNER_CD\"::text, 6, '0')), '.jpg');")

        ## Adding field 'Brand.brand_logo'
        #media = urlparse.urlparse(settings.MEDIA_URL)
        #for owner in BrandOwner.objects.all():
        #    if hasattr(owner.owner_logo, 'url'):
        #        if not http_destination_exists(media.netloc,
        #            urlparse.urljoin(media.path, owner.owner_logo.name)):
        #            print "Owner logo could not be found ( %s )" % owner.owner_logo.name
        #            owner.owner_logo = None
        #            owner.save()


    def backwards(self, orm):
        # Deleting field 'Brand.brand_logo'
        pass


    models = {
        u'brand.brand': {
            'Meta': {'ordering': "[u'brand_nm']", 'unique_together': "((u'brand_nm', u'owner_cd'),)", 'object_name': 'Brand', 'db_table': "u'brand'"},
            'brand_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'db_column': "u'BRAND_LINK'", 'blank': 'True'}),
            'brand_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'db_column': "u'BRAND_LOGO'", 'blank': 'True'}),
            'brand_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_NM'"}),
            'brand_type_cd': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brand.BrandType']", 'db_column': "u'BRAND_TYPE_CD'"}),
            'bsin': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'BSIN'"}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "u'COMMENTS'", 'blank': 'True'}),
            'flag_delete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'FLAG_DELETE'"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "u'LAST_MODIFIED'", 'blank': 'True'}),
            'owner_cd': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brand.BrandOwner']", 'null': 'True', 'db_column': "u'OWNER_CD'", 'blank': 'True'})
        },
        u'brand.brandowner': {
            'Meta': {'ordering': "[u'owner_nm']", 'object_name': 'BrandOwner', 'db_table': "u'brand_owner'"},
            'owner_cd': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'OWNER_CD'"}),
            'owner_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'db_column': "u'OWNER_LINK'", 'blank': 'True'}),
            'owner_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'db_column': "u'OWNER_LOGO'", 'blank': 'True'}),
            'owner_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'OWNER_NM'"}),
            'owner_wiki_en': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'db_column': "u'OWNER_WIKI_EN'", 'blank': 'True'})
        },
        u'brand.brandtype': {
            'Meta': {'object_name': 'BrandType', 'db_table': "u'brand_type'"},
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'BRAND_TYPE_CD'"}),
            'brand_type_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_TYPE_NM'"})
        }
    }

    complete_apps = ['brand']
