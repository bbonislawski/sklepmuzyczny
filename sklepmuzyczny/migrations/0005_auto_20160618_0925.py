# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-18 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklepmuzyczny', '0004_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adres',
            new_name='kodpocztowy',
        ),
        migrations.AddField(
            model_name='order',
            name='miasto',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
