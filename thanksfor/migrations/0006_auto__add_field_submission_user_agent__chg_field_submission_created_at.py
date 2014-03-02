# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Submission.user_agent'
        db.add_column(u'thanksfor_submission', 'user_agent',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Submission.created_at'
        db.alter_column(u'thanksfor_submission', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Deleting field 'Submission.user_agent'
        db.delete_column(u'thanksfor_submission', 'user_agent')


        # Changing field 'Submission.created_at'
        db.alter_column(u'thanksfor_submission', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'thanksfor.submission': {
            'Meta': {'object_name': 'Submission'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'show_in_site': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['thanksfor']