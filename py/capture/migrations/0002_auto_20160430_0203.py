# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayspringuser',
            name='id_type',
            field=models.CharField(max_length=10, choices=[(b'nric', b'NRIC'), (b'fin', b'FIN')]),
        ),
        migrations.AlterField(
            model_name='dayspringuser',
            name='salutation',
            field=models.CharField(max_length=5, choices=[(b'mr', b'Mr'), (b'ms', b'Ms'), (b'dr', b'Dr'), (b'mrs', b'Mrs')]),
        ),
        migrations.AlterField(
            model_name='donation',
            name='name_of_fund',
            field=models.CharField(max_length=20, choices=[(b'ds_tax', b'DS TAX'), (b'ds_nlc', b'DS NLC')]),
        ),
        migrations.AlterField(
            model_name='donation',
            name='payment_type',
            field=models.CharField(max_length=200, verbose_name=((b'cash', b'Cash'), (b'paypal', b'PayPal'), (b'cheque', b'Cheque'))),
        ),
        migrations.AlterField(
            model_name='donation',
            name='type_of_donation',
            field=models.CharField(max_length=200, verbose_name=((b'oc', b'Outright Cash'), (b'credit', b'Credit'))),
        ),
    ]
