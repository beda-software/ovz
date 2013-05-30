# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table(u'schools_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('contacts', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('establishing', self.gf('ckeditor.fields.RichTextField')()),
            ('specialties', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('rules', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('advanced', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'schools', ['School'])

        # Adding M2M table for field professions on 'School'
        db.create_table(u'schools_school_professions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('school', models.ForeignKey(orm[u'schools.school'], null=False)),
            ('profession', models.ForeignKey(orm[u'your_choice.profession'], null=False))
        ))
        db.create_unique(u'schools_school_professions', ['school_id', 'profession_id'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table(u'schools_school')

        # Removing M2M table for field professions on 'School'
        db.delete_table('schools_school_professions')


    models = {
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            'advanced': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'establishing': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'professions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['your_choice.Profession']", 'symmetrical': 'False'}),
            'rules': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'specialties': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'your_choice.profession': {
            'Meta': {'object_name': 'Profession'},
            'ability': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['your_choice.ProfessionAbility']", 'null': 'True', 'blank': 'True'}),
            'characteristic': ('ckeditor.fields.RichTextField', [], {}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'contraindications': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['your_choice.ProfessionContraindications']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['schools']