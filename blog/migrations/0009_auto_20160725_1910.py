# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_weave_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeratinBond_Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('weave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Weave')),
            ],
        ),
        migrations.CreateModel(
            name='MicroRing_Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TapedHairExtention_Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('weave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Weave')),
            ],
        ),
        migrations.DeleteModel(
            name='HairExtention',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.RemoveField(
            model_name='keratinbond',
            name='price',
        ),
        migrations.RemoveField(
            model_name='microring',
            name='price',
        ),
        migrations.RemoveField(
            model_name='tapedhairextention',
            name='price',
        ),
        migrations.AddField(
            model_name='microring_price',
            name='microRing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.MicroRing'),
        ),
    ]
