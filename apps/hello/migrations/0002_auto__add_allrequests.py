# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AllRequests'
        db.create_table('hello_allrequests', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('server_protocol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status_code', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('content_len', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
        ))
        db.send_create_signal('hello', ['AllRequests'])


    def backwards(self, orm):
        # Deleting model 'AllRequests'
        db.delete_table('hello_allrequests')


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
            'Meta': {'object_name': 'AllRequests', 'ordering': "['date_time']"},
            'content_len': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['hello']