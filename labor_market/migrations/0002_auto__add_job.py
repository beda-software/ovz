# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table(u'labor_market_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('ckeditor.fields.RichTextField')()),
            ('contacts', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('create', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'labor_market', ['Job'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table(u'labor_market_job')


    models = {
        u'labor_market.job': {
            'Meta': {'object_name': 'Job'},
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'create': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['labor_market']