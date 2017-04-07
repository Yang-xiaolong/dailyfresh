# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='g_pic',
            field=models.ImageField(upload_to=b'goods'),
        ),
    ]
