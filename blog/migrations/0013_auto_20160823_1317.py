# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-23 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160813_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keratinbond_price',
            name='weave',
        ),
        migrations.RemoveField(
            model_name='microring_price',
            name='microRing',
        ),
        migrations.RemoveField(
            model_name='pricee',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='tapedhairextention_price',
            name='weave',
        ),
        migrations.RemoveField(
            model_name='weave_price',
            name='weave',
        ),
        migrations.DeleteModel(
            name='KeratinBond_Price',
        ),
        migrations.DeleteModel(
            name='MicroRing_Price',
        ),
        migrations.DeleteModel(
            name='Pricee',
        ),
        migrations.DeleteModel(
            name='TapedHairExtention_Price',
        ),
        migrations.DeleteModel(
            name='Weave_Price',
        ),
    ]