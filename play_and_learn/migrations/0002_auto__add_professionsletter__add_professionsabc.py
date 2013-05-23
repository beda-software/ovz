# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProfessionsLetter'
        db.create_table(u'play_and_learn_professionsletter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('letter', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('letter_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'play_and_learn', ['ProfessionsLetter'])

        # Adding model 'ProfessionsABC'
        db.create_table(u'play_and_learn_professionsabc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('first_letter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['play_and_learn.ProfessionsLetter'], null=True, blank=True)),
        ))
        db.send_create_signal(u'play_and_learn', ['ProfessionsABC'])


    def backwards(self, orm):
        # Deleting model 'ProfessionsLetter'
        db.delete_table(u'play_and_learn_professionsletter')

        # Deleting model 'ProfessionsABC'
        db.delete_table(u'play_and_learn_professionsabc')


    models = {
        u'play_and_learn.professionsabc': {
            'Meta': {'object_name': 'ProfessionsABC'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'first_letter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['play_and_learn.ProfessionsLetter']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'play_and_learn.professionsletter': {
            'Meta': {'object_name': 'ProfessionsLetter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'letter_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['play_and_learn']