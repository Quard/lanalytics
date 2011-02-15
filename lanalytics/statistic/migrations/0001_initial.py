# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Browser'
        db.create_table('statistic_browser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('statistic', ['Browser'])

        # Adding model 'OS'
        db.create_table('statistic_os', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('statistic', ['OS'])

        # Adding model 'Refferrer'
        db.create_table('statistic_refferrer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('statistic', ['Refferrer'])

        # Adding model 'ScreenResolution'
        db.create_table('statistic_screenresolution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('resolution', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal('statistic', ['ScreenResolution'])


    def backwards(self, orm):
        
        # Deleting model 'Browser'
        db.delete_table('statistic_browser')

        # Deleting model 'OS'
        db.delete_table('statistic_os')

        # Deleting model 'Refferrer'
        db.delete_table('statistic_refferrer')

        # Deleting model 'ScreenResolution'
        db.delete_table('statistic_screenresolution')


    models = {
        'statistic.browser': {
            'Meta': {'object_name': 'Browser'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'statistic.os': {
            'Meta': {'object_name': 'OS'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'statistic.refferrer': {
            'Meta': {'object_name': 'Refferrer'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'statistic.screenresolution': {
            'Meta': {'object_name': 'ScreenResolution'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'resolution': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        }
    }

    complete_apps = ['statistic']
