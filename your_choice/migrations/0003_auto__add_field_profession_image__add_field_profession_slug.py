# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Profession.image'
        db.add_column(u'your_choice_profession', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Profession.slug'
        db.add_column(u'your_choice_profession', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='slug', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Profession.image'
        db.delete_column(u'your_choice_profession', 'image')

        # Deleting field 'Profession.slug'
        db.delete_column(u'your_choice_profession', 'slug')


    models = {
        u'your_choice.profession': {
            'Meta': {'object_name': 'Profession'},
            'ability': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['your_choice.ProfessionAbility']", 'null': 'True', 'blank': 'True'}),
            'characteristic': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'contraindications': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['your_choice.ProfessionContraindications']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'your_choice.professionability': {
            'Meta': {'object_name': 'ProfessionAbility'},
            'ability': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'your_choice.professioncontraindications': {
            'Meta': {'object_name': 'ProfessionContraindications'},
            'contraindication': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['your_choice']