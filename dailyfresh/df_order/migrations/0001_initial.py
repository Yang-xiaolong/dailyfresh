# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0003_auto_20170406_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='OderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='df_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('o_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('o_date', models.DateField(auto_now=True)),
                ('o_subtotal', models.DecimalField(max_digits=8, decimal_places=2)),
                ('o_address', models.CharField(max_length=150)),
                ('o_is_pay', models.BooleanField(default=False)),
                ('o_user', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='oderdetailinfo',
            name='order',
            field=models.ForeignKey(to='df_order.OrderInfo'),
        ),
    ]
