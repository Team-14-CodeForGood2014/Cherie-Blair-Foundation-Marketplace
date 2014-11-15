# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchEngine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='redundant',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
