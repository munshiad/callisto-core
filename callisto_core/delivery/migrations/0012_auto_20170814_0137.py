# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 01:37
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0011_report_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
