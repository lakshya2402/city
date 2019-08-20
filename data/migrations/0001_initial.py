# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-20 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=250)),
                ('store_address', models.CharField(max_length=250)),
                ('store_contact_no', models.IntegerField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='storedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.store')),
            ],
        ),
    ]
