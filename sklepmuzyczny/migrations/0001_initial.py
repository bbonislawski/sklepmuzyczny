# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-03 13:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Disc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('available_count', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('carts', models.ManyToManyField(to='sklepmuzyczny.Cart')),
            ],
        ),
    ]
