# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 06:13
from __future__ import unicode_literals

from django.db import migrations, models

import callisto_core.wizard_builder.model_helpers


class Migration(migrations.Migration):

    dependencies = [
        ('wizard_builder', '0038_checkbox_radiobutton'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dropdown',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=(
                callisto_core.wizard_builder.model_helpers.ProxyQuestion,
                'wizard_builder.formquestion'),
        ),
        migrations.AlterField(
            model_name='formquestion',
            name='type',
            field=models.TextField(
                choices=[
                    ('checkbox',
                     'checkbox'),
                    ('dropdown',
                     'dropdown'),
                    ('radiobutton',
                     'radiobutton'),
                    ('singlelinetext',
                     'singlelinetext'),
                    ('textarea',
                     'textarea')],
                default='singlelinetext',
                null=True),
        ),
    ]
