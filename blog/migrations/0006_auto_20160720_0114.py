# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 00:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_keratinbonds_microrings_tapedhairextentions_weave'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KeratinBonds',
            new_name='KeratinBond',
        ),
        migrations.RenameModel(
            old_name='MicroRings',
            new_name='MicroRing',
        ),
        migrations.RenameModel(
            old_name='TapedHairExtentions',
            new_name='TapedHairExtention',
        ),
    ]
