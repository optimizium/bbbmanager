# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=80)),
                ('role', models.CharField(max_length=20)),
                ('timezone', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('state', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('street', models.TextField(null=True, blank=True)),
                ('pin', models.CharField(max_length=30, null=True, blank=True)),
                ('user_type', models.CharField(max_length=100)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('primary_mobile', models.CharField(max_length=100, null=True, blank=True)),
                ('secondary_mobile', models.CharField(max_length=100, null=True, blank=True)),
                ('primary_email', models.CharField(max_length=100, null=True, blank=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('date_modified', models.DateTimeField(null=True)),
                ('org_name', models.ForeignKey(related_name=b'user_org_nm', to='organization.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
