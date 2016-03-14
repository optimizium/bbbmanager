# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20160220_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='contact_no',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
