# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MethodicalBank'
        db.create_table(u'methodical_bank_methodicalbank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('about_author', self.gf('ckeditor.fields.RichTextField')()),
            ('methodology', self.gf('ckeditor.fields.RichTextField')()),
            ('attached', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('create', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'methodical_bank', ['MethodicalBank'])


    def backwards(self, orm):
        # Deleting model 'MethodicalBank'
        db.delete_table(u'methodical_bank_methodicalbank')


    models = {
        u'methodical_bank.methodicalbank': {
            'Meta': {'object_name': 'MethodicalBank'},
            'about_author': ('ckeditor.fields.RichTextField', [], {}),
            'attached': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'create': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'methodology': ('ckeditor.fields.RichTextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['methodical_bank']