# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='notification_url',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='password',
        ),
        migrations.AddField(
            model_name='participant',
            name='previlage',
            field=models.CharField(default=b'attendee', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participant',
            name='meeting_id',
            field=models.ForeignKey(related_name=b'meeting_participants', to='meetings.Meeting'),
        ),
    ]
