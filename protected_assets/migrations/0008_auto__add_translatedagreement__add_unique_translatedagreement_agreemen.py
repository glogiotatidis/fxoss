# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TranslatedAgreement'
        db.create_table(u'protected_assets_translatedagreement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agreement', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['protected_assets.Agreement'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('agreement_pdf', self.gf('django.db.models.fields.files.FileField')(max_length=255)),
        ))
        db.send_create_signal(u'protected_assets', ['TranslatedAgreement'])

        # Adding unique constraint on 'TranslatedAgreement', fields ['agreement', 'language']
        db.create_unique(u'protected_assets_translatedagreement', ['agreement_id', 'language'])


    def backwards(self, orm):
        # Removing unique constraint on 'TranslatedAgreement', fields ['agreement', 'language']
        db.delete_unique(u'protected_assets_translatedagreement', ['agreement_id', 'language'])

        # Deleting model 'TranslatedAgreement'
        db.delete_table(u'protected_assets_translatedagreement')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'protected_assets.agreement': {
            'Meta': {'object_name': 'Agreement'},
            'agreement_pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Prototype Branding Agreement'", 'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'protected_assets.signedagreement': {
            'Meta': {'ordering': "['-timestamp']", 'unique_together': "(('user', 'agreement'),)", 'object_name': 'SignedAgreement'},
            'agreement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protected_assets.Agreement']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'protected_assets.translatedagreement': {
            'Meta': {'unique_together': "(('agreement', 'language'),)", 'object_name': 'TranslatedAgreement'},
            'agreement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': u"orm['protected_assets.Agreement']"}),
            'agreement_pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['protected_assets']