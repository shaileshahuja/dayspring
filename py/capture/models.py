from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from py import static

from datetime import date


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class DaySpringUser(User):
    salutation = models.CharField(choices=static.SALUTATIONS, max_length=5)
    address = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=6)
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(choices=static.GENDERS, max_length=10)
    birthday = models.DateField()
    id_type = models.CharField(choices=static.ID_TYPES, max_length=10)
    id_no = models.CharField(max_length=10, unique=True)
    age = models.PositiveIntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.age = calculate_age(self.birthday)
        super(DaySpringUser, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                        update_fields=update_fields)


class DaySpringProject(models.Model):
    name = models.CharField(choices=static.PROJECT_NAMES, max_length=200)


class Donation(models.Model):
    payment_type = models.CharField(static.PAYMENT_TYPES, max_length=200)
    type_of_donation = models.CharField(static.DONATION_TYPES, max_length=200)
    donation_date = models.DateField()
    payment_number = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    prefix = models.CharField(max_length=10)
    receipt_serial_no = models.CharField(max_length=10)
    date_printing = models.DateField()
    print_indicator = models.CharField(max_length=1)
    void = models.BooleanField()
    converted = models.BooleanField()
    name_of_fund = models.CharField(choices=static.FUND_NAMES, max_length=20)
    remarks = models.CharField(max_length=500, null=True, blank=True)
    project = models.ForeignKey(to=DaySpringProject)
    user = models.ForeignKey(to=DaySpringUser)
    individual_indicator = models.BooleanField()
