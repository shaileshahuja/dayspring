# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0002_combined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combined',
            name='id_no',
            field=models.CharField(max_length=10),
        ),
    ]
