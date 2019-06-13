# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-06-13 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('other_name', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('email', models.EmailField(blank=True, max_length=20, null=True)),
                ('identity_number', models.CharField(max_length=20, unique=True)),
                ('language_code', models.CharField(default='en', max_length=5)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.State')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
