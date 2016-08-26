# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('TasksManager_userprofile', (
            ('user_auth', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, primary_key=True, to=orm['auth.User'])),
            ('phone', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, blank=True, null=True)),
            ('born_date', self.gf('django.db.models.fields.DateField')(default=None, blank=True, null=True)),
            ('last_connexion', self.gf('django.db.models.fields.DateTimeField')(default=None, blank=True, null=True)),
            ('years_seniority', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('TasksManager', ['UserProfile'])

        # Adding model 'Supervisor'
        db.create_table('TasksManager_supervisor', (
            ('userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, primary_key=True, to=orm['TasksManager.UserProfile'])),
            ('specialisation', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('TasksManager', ['Supervisor'])

        # Adding model 'Developer'
        db.create_table('TasksManager_developer', (
            ('userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, primary_key=True, to=orm['TasksManager.UserProfile'])),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TasksManager.Supervisor'])),
        ))
        db.send_create_signal('TasksManager', ['Developer'])

        # Adding model 'Project'
        db.create_table('TasksManager_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('client_name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('TasksManager', ['Project'])

        # Adding model 'Task'
        db.create_table('TasksManager_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('time_elapsed', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True, null=True)),
            ('importance', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(default=None, blank=True, to=orm['TasksManager.Project'], null=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TasksManager.Developer'])),
        ))
        db.send_create_signal('TasksManager', ['Task'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('TasksManager_userprofile')

        # Deleting model 'Supervisor'
        db.delete_table('TasksManager_supervisor')

        # Deleting model 'Developer'
        db.delete_table('TasksManager_developer')

        # Deleting model 'Project'
        db.delete_table('TasksManager_project')

        # Deleting model 'Task'
        db.delete_table('TasksManager_task')


    models = {
        'TasksManager.developer': {
            'Meta': {'_ormbases': ['TasksManager.UserProfile'], 'object_name': 'Developer'},
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['TasksManager.Supervisor']"}),
            'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['TasksManager.UserProfile']"})
        },
        'TasksManager.project': {
            'Meta': {'object_name': 'Project'},
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'TasksManager.supervisor': {
            'Meta': {'_ormbases': ['TasksManager.UserProfile'], 'object_name': 'Supervisor'},
            'specialisation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['TasksManager.UserProfile']"})
        },
        'TasksManager.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['TasksManager.Developer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'blank': 'True', 'to': "orm['TasksManager.Project']", 'null': 'True'}),
            'time_elapsed': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'TasksManager.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'born_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'last_connexion': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'user_auth': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['auth.User']"}),
            'years_seniority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['TasksManager']