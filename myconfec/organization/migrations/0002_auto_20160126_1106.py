# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='primary_email',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='primary_landline',
        ),
        migrations.AddField(
            model_name='organization',
            name='email',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_url',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
