# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AllRequests.priority'
        db.add_column('hello_allrequests', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=1, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AllRequests.priority'
        db.delete_column('hello_allrequests', 'priority')


    models = {
        'hello.about_me': {
            'Meta': {'object_name': 'About_me'},
            'bio': ('django.db.models.fields.CharField', [], {'default': "'bio'", 'max_length': '500'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'contacts': ('django.db.models.fields.CharField', [], {'default': "'contacts'", 'max_length': '150'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'default': "'id'", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '33'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "'skype'", 'max_length': '33'}),
            'surname': ('django.db.models.fields.CharField', [], {'default': "'surname'", 'max_length': '33'})
        },
        'hello.allrequests': {
            'Meta': {'ordering': "['date_time']", 'object_name': 'AllRequests'},
            'content_len': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'hello.changeslog': {
            'Meta': {'object_name': 'ChangesLog'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'operation': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['hello']