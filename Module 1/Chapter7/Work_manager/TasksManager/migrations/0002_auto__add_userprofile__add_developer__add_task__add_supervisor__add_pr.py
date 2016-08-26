# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('TasksManager_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(blank=True, default=None, max_length=20, null=True)),
            ('born_date', self.gf('django.db.models.fields.DateField')(blank=True, default=None, null=True)),
            ('last_connection', self.gf('django.db.models.fields.DateTimeField')(blank=True, default=None, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('years_seniority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_created', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('TasksManager', ['UserProfile'])

        # Adding model 'Developer'
        db.create_table('TasksManager_developer', (
            ('userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['TasksManager.UserProfile'], unique=True)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TasksManager.Supervisor'])),
        ))
        db.send_create_signal('TasksManager', ['Developer'])

        # Adding model 'Task'
        db.create_table('TasksManager_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('time_elapsed', self.gf('django.db.models.fields.IntegerField')(blank=True, default=None, null=True)),
            ('importance', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, default=None, to=orm['TasksManager.Project'], null=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TasksManager.Developer'])),
        ))
        db.send_create_signal('TasksManager', ['Task'])

        # Adding model 'Supervisor'
        db.create_table('TasksManager_supervisor', (
            ('userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['TasksManager.UserProfile'], unique=True)),
            ('specialisation', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('TasksManager', ['Supervisor'])

        # Adding model 'Project'
        db.create_table('TasksManager_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('client_name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('TasksManager', ['Project'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('TasksManager_userprofile')

        # Deleting model 'Developer'
        db.delete_table('TasksManager_developer')

        # Deleting model 'Task'
        db.delete_table('TasksManager_task')

        # Deleting model 'Supervisor'
        db.delete_table('TasksManager_supervisor')

        # Deleting model 'Project'
        db.delete_table('TasksManager_project')


    models = {
        'TasksManager.developer': {
            'Meta': {'object_name': 'Developer', '_ormbases': ['TasksManager.UserProfile']},
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['TasksManager.Supervisor']"}),
            'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['TasksManager.UserProfile']", 'unique': 'True'})
        },
        'TasksManager.project': {
            'Meta': {'object_name': 'Project'},
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'TasksManager.supervisor': {
            'Meta': {'object_name': 'Supervisor', '_ormbases': ['TasksManager.UserProfile']},
            'specialisation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['TasksManager.UserProfile']", 'unique': 'True'})
        },
        'TasksManager.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['TasksManager.Developer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'default': 'None', 'to': "orm['TasksManager.Project']", 'null': 'True'}),
            'time_elapsed': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'TasksManager.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'born_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_connection': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': 'None', 'max_length': '20', 'null': 'True'}),
            'years_seniority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['TasksManager']