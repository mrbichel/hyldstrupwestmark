# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Signup.address'
        db.add_column('courses_signup', 'address',
                      self.gf('django.db.models.fields.TextField')(default='none'),
                      keep_default=False)

        # Adding field 'Signup.postal_code'
        db.add_column('courses_signup', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=20),
                      keep_default=False)

        # Adding field 'Signup.country'
        db.add_column('courses_signup', 'country',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=40),
                      keep_default=False)

        # Adding field 'Signup.profession'
        db.add_column('courses_signup', 'profession',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Signup.address'
        db.delete_column('courses_signup', 'address')

        # Deleting field 'Signup.postal_code'
        db.delete_column('courses_signup', 'postal_code')

        # Deleting field 'Signup.country'
        db.delete_column('courses_signup', 'country')

        # Deleting field 'Signup.profession'
        db.delete_column('courses_signup', 'profession')

    models = {
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '55'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'courses.occurrence': {
            'Meta': {'object_name': 'Occurrence'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['courses.Course']"}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'courses.signup': {
            'Meta': {'object_name': 'Signup'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'occurrence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['courses.Occurrence']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['courses']