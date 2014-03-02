# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Submission.raw_image'
        db.delete_column(u'thanksfor_submission', 'raw_image')

        # Adding field 'Submission.image'
        db.add_column(u'thanksfor_submission', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Submission.raw_image'
        db.add_column(u'thanksfor_submission', 'raw_image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Submission.image'
        db.delete_column(u'thanksfor_submission', 'image')


    models = {
        u'thanksfor.submission': {
            'Meta': {'object_name': 'Submission'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'show_in_site': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['thanksfor']