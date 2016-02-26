# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org_name', models.CharField(max_length=30)),
                ('org_type', models.CharField(max_length=30, null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('org_url', models.CharField(max_length=120)),
                ('notes', models.TextField(null=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('state', models.CharField(max_length=50, null=True, blank=True)),
                ('country', models.CharField(max_length=50, null=True, blank=True)),
                ('street', models.TextField(null=True, blank=True)),
                ('pin', models.CharField(max_length=30, null=True, blank=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('is_activated', models.BooleanField(default=False)),
                ('primary_mobile', models.CharField(max_length=100)),
                ('primary_landline', models.CharField(max_length=100)),
                ('primary_email', models.CharField(max_length=100)),
                ('org_pin', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
