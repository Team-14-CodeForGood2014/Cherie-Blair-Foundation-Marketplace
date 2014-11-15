# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchEngine', '0002_search_redundant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='redundant',
        ),
    ]
