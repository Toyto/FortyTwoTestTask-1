# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'About_me'
        db.create_table('hello_about_me', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=33, default='name')),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=33, default='surname')),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=500, default='bio')),
            ('contacts', self.gf('django.db.models.fields.CharField')(max_length=150, default='contacts')),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=50, default='id')),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=33, default='skype')),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('hello', ['About_me'])


    def backwards(self, orm):
        # Deleting model 'About_me'
        db.delete_table('hello_about_me')


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
        }
    }

    complete_apps = ['hello']