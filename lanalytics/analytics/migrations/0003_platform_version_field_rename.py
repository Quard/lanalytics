# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Analytic.platrorm_version'
        db.delete_column('analytics_analytic', 'platrorm_version')

        # Adding field 'Analytic.platform_version'
        db.add_column('analytics_analytic', 'platform_version', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True), keep_default=False)

        # Changing field 'Analytic.platform'
        db.alter_column('analytics_analytic', 'platform', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Analytic.browser_version'
        db.alter_column('analytics_analytic', 'browser_version', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))


    def backwards(self, orm):
        
        # Adding field 'Analytic.platrorm_version'
        db.add_column('analytics_analytic', 'platrorm_version', self.gf('django.db.models.fields.CharField')(default=2, max_length=15), keep_default=False)

        # Deleting field 'Analytic.platform_version'
        db.delete_column('analytics_analytic', 'platform_version')

        # Changing field 'Analytic.platform'
        db.alter_column('analytics_analytic', 'platform', self.gf('django.db.models.fields.CharField')(default=None, max_length=20))

        # Changing field 'Analytic.browser_version'
        db.alter_column('analytics_analytic', 'browser_version', self.gf('django.db.models.fields.CharField')(default=None, max_length=15))


    models = {
        'analytics.analytic': {
            'Meta': {'object_name': 'Analytic'},
            'browser': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'browser_version': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled_cookie': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'have_flash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'have_java': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'platform_version': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'refferrer': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'screen_resolution': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'analytics'", 'to': "orm['statistic.Site']"}),
            'time_zone': ('django.db.models.fields.IntegerField', [], {}),
            'visitor': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'window_dimensions': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'statistic.site': {
            'Meta': {'object_name': 'Site'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sites'", 'to': "orm['auth.User']"}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['analytics']
