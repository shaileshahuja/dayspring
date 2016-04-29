# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaySpringUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('salutation', models.CharField(max_length=5, choices=[(b'mr', b'Mr'), (b'ms', b'Ms')])),
                ('address', models.CharField(max_length=300)),
                ('postal_code', models.CharField(max_length=6)),
                ('contact_no', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10, choices=[(b'm', b'Male'), (b'f', b'Female')])),
                ('birthday', models.DateField()),
                ('id_type', models.CharField(max_length=10, choices=[(b'paypal', b'Paypal'), (b'cash', b'Cash')])),
                ('id_no', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_type', models.CharField(max_length=200, verbose_name=((b'paypal', b'Paypal'), (b'cash', b'Cash')))),
                ('type_of_donation', models.CharField(max_length=200, verbose_name=((b'paypal', b'Paypal'), (b'cash', b'Cash')))),
                ('amount', models.PositiveIntegerField()),
                ('prefix', models.CharField(max_length=10)),
                ('receipt_serial_no', models.CharField(max_length=10)),
                ('date_printing', models.DateField()),
                ('print_indicator', models.CharField(max_length=1)),
                ('void', models.BooleanField()),
                ('converted', models.BooleanField()),
                ('name_of_fund', models.CharField(max_length=20, choices=[(b'paypal', b'Paypal'), (b'cash', b'Cash')])),
                ('remarks', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='project',
            field=models.ForeignKey(to='capture.Project'),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(to='capture.DaySpringUser'),
        ),
    ]
