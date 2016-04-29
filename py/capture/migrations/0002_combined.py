# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combined',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_type', models.CharField(max_length=200, verbose_name=((b'Cash', b'Cash'), (b'PayPal', b'PayPal'), (b'Cheque', b'Cheque')))),
                ('type_of_donation', models.CharField(max_length=200, verbose_name=((b'Outright Cash', b'Outright Cash'), (b'Credit', b'Credit')))),
                ('donation_date', models.DateField()),
                ('payment_number', models.CharField(max_length=200)),
                ('amount', models.PositiveIntegerField()),
                ('prefix', models.CharField(max_length=10)),
                ('receipt_serial_no', models.CharField(max_length=10)),
                ('date_printing', models.DateField()),
                ('print_indicator', models.CharField(max_length=1)),
                ('void', models.BooleanField()),
                ('converted', models.BooleanField()),
                ('name_of_fund', models.CharField(max_length=20, choices=[(b'DS TAX', b'DS TAX'), (b'DS NLC', b'DS NLC')])),
                ('remarks', models.CharField(max_length=500, null=True, blank=True)),
                ('project_name', models.CharField(max_length=200, choices=[(b'FB GIT Hackathon', b'FB GIT Hackathon'), (b'Message of Hope', b'Message of Hope'), (b'Empowerment', b'Empowerment'), (b'Ray of Hope', b'Ray of Hope'), (b'Donate Now', b'Donate Now'), (b'FB GIT Hackathon 2', b'FB GIT Hackathon 2'), (b'Message of Hope', b'Message of Hope 2'), (b'Empowerment 2', b'Empowerment 2'), (b'Ray of Hope 2', b'Ray of Hope 2'), (b'Donate Now 2', b'Donate Now 2')])),
                ('salutation', models.CharField(max_length=5, choices=[(b'mr', b'Mr'), (b'ms', b'Ms'), (b'dr', b'Dr'), (b'mrs', b'Mrs')])),
                ('address', models.CharField(max_length=300)),
                ('postal_code', models.CharField(max_length=6)),
                ('contact_no', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('birthday', models.DateField()),
                ('id_type', models.CharField(max_length=10, choices=[(b'NRIC', b'NRIC'), (b'FIN', b'FIN')])),
                ('id_no', models.CharField(unique=True, max_length=10)),
                ('age', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
    ]
