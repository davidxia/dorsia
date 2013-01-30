# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reservation'
        db.create_table('dorsia_reservation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('partySize', self.gf('django.db.models.fields.IntegerField')()),
            ('reservationDate', self.gf('django.db.models.fields.DateField')()),
            ('seatingTime', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('dorsia', ['Reservation'])


    def backwards(self, orm):
        # Deleting model 'Reservation'
        db.delete_table('dorsia_reservation')


    models = {
        'dorsia.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partySize': ('django.db.models.fields.IntegerField', [], {}),
            'reservationDate': ('django.db.models.fields.DateField', [], {}),
            'seatingTime': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['dorsia']