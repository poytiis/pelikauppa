# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelikauppa', '0004_auto_20170423_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameownerships',
            name='high_score',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
