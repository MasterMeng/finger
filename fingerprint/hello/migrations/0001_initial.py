# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('finger', models.CharField(max_length=20, null=True)),
                ('os', models.CharField(max_length=20, null=True)),
                ('os_ver', models.CharField(max_length=20, null=True)),
                ('browser', models.CharField(max_length=20, null=True)),
                ('browser_ver', models.CharField(max_length=20, null=True)),
                ('CPU', models.CharField(max_length=20, null=True)),
                ('device', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
