# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uName', models.CharField(max_length=20)),
                ('uPassword', models.CharField(max_length=40)),
                ('uEmail', models.CharField(max_length=30)),
                ('uAddressee', models.CharField(default=b'', max_length=20)),
                ('uAddress', models.CharField(default=b'', max_length=100)),
                ('uZipCode', models.CharField(default=b'', max_length=6)),
                ('uPhone', models.CharField(default=b'', max_length=11)),
            ],
        ),
    ]
