# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChangesLog'
        db.create_table('hello_changeslog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('operation', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('hello', ['ChangesLog'])


    def backwards(self, orm):
        # Deleting model 'ChangesLog'
        db.delete_table('hello_changeslog')


    models = {
        'hello.about_me': {
            'Meta': {'object_name': 'About_me'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "'bio'"}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '150', 'default': "'contacts'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'id'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '33', 'default': "'name'"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '33', 'default': "'skype'"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '33', 'default': "'surname'"})
        },
        'hello.allrequests': {
            'Meta': {'ordering': "['date_time']", 'object_name': 'AllRequests'},
            'content_len': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'hello.changeslog': {
            'Meta': {'object_name': 'ChangesLog'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'operation': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['hello']