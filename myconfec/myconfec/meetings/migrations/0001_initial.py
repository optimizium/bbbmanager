# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('meetingID', models.CharField(max_length=50)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('attendee_passwd', models.CharField(max_length=100)),
                ('moderator_passwd', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('meeting_datetime', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('meeting_duration', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=20)),
                ('conferenceID', models.IntegerField(null=True, blank=True)),
                ('meeting_logout_url', models.CharField(max_length=100)),
                ('max_participants', models.IntegerField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name=b'meetingroom_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('type', models.CharField(max_length=200, null=True, blank=True)),
                ('expired_on', models.CharField(max_length=100, blank=True)),
                ('user', models.ForeignKey(related_name=b'meeting_created', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('notification_url', models.CharField(max_length=250)),
                ('user_view_url', models.CharField(max_length=300)),
                ('contact_no', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=100, null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=200)),
                ('meeting_id', models.ForeignKey(related_name=b'attendee', to='meetings.Meeting')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='meeting',
            name='venue',
            field=models.ForeignKey(related_name=b'meetingroom', blank=True, to='meetings.MeetingRoom', null=True),
            preserve_default=True,
        ),
    ]
