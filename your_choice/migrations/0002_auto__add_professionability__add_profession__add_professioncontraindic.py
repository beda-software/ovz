# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProfessionAbility'
        db.create_table(u'your_choice_professionability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ability', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'your_choice', ['ProfessionAbility'])

        # Adding model 'Profession'
        db.create_table(u'your_choice_profession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('characteristic', self.gf('ckeditor.fields.RichTextField')()),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'your_choice', ['Profession'])

        # Adding M2M table for field ability on 'Profession'
        db.create_table(u'your_choice_profession_ability', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profession', models.ForeignKey(orm[u'your_choice.profession'], null=False)),
            ('professionability', models.ForeignKey(orm[u'your_choice.professionability'], null=False))
        ))
        db.create_unique(u'your_choice_profession_ability', ['profession_id', 'professionability_id'])

        # Adding M2M table for field contraindications on 'Profession'
        db.create_table(u'your_choice_profession_contraindications', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profession', models.ForeignKey(orm[u'your_choice.profession'], null=False)),
            ('professioncontraindications', models.ForeignKey(orm[u'your_choice.professioncontraindications'], null=False))
        ))
        db.create_unique(u'your_choice_profession_contraindications', ['profession_id', 'professioncontraindications_id'])

        # Adding model 'ProfessionContraindications'
        db.create_table(u'your_choice_professioncontraindications', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contraindication', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'your_choice', ['ProfessionContraindications'])


    def backwards(self, orm):
        # Deleting model 'ProfessionAbility'
        db.delete_table(u'your_choice_professionability')

        # Deleting model 'Profession'
        db.delete_table(u'your_choice_profession')

        # Removing M2M table for field ability on 'Profession'
        db.delete_table('your_choice_profession_ability')

        # Removing M2M table for field contraindications on 'Profession'
        db.delete_table('your_choice_profession_contraindications')

        # Deleting model 'ProfessionContraindications'
        db.delete_table(u'your_choice_professioncontraindications')


    models = {
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

    complete_apps = ['your_choice']