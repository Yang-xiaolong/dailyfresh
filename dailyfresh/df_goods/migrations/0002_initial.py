# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('g_title', models.CharField(max_length=20)),
                ('g_pic', models.ImageField(upload_to=b'df_goods')),
                ('g_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('g_unit', models.CharField(default=b'500g', max_length=20)),
                ('g_click', models.IntegerField()),
                ('g_profiles', models.CharField(max_length=200)),
                ('g_stock', models.IntegerField()),
                ('g_content', tinymce.models.HTMLField()),
                ('g_is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]
