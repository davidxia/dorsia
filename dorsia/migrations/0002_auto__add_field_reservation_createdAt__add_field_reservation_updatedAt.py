# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reservation.createdAt'
        db.add_column('dorsia_reservation', 'createdAt',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Reservation.updatedAt'
        db.add_column('dorsia_reservation', 'updatedAt',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reservation.createdAt'
        db.delete_column('dorsia_reservation', 'createdAt')

        # Deleting field 'Reservation.updatedAt'
        db.delete_column('dorsia_reservation', 'updatedAt')


    models = {
        'dorsia.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'createdAt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partySize': ('django.db.models.fields.IntegerField', [], {}),
            'reservationDate': ('django.db.models.fields.DateField', [], {}),
            'seatingTime': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'updatedAt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dorsia']