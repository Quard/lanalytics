# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Analytic'
        db.create_table('analytics_analytic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visitor', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('browser', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('browser_version', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('platrorm_version', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('time_zone', self.gf('django.db.models.fields.IntegerField')()),
            ('screen_resolution', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('window_dimensions', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('enabled_cookie', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('have_flash', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('have_java', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('refferrer', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('analytics', ['Analytic'])


    def backwards(self, orm):
        
        # Deleting model 'Analytic'
        db.delete_table('analytics_analytic')


    models = {
        'analytics.analytic': {
            'Meta': {'object_name': 'Analytic'},
            'browser': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'browser_version': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled_cookie': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'have_flash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'have_java': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'platrorm_version': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'refferrer': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'screen_resolution': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'time_zone': ('django.db.models.fields.IntegerField', [], {}),
            'visitor': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'window_dimensions': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        }
    }

    complete_apps = ['analytics']
