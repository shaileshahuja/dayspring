from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from py import static


class DaySpringUser(User):
    salutation = models.CharField(choices=static.SALUTATIONS, max_length=5)
    address = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=6)
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(choices=static.GENDERS, max_length=10)
    birthday = models.DateField()
    id_type = models.CharField(choices=static.ID_TYPES, max_length=10)
    id_no = models.CharField(max_length=10)
    age = models.PositiveIntegerField()


class Project(models.Model):
    name = models.CharField(max_length=200)


class Donation(models.Model):
    payment_type = models.CharField(static.PAYMENT_TYPES, max_length=200)
    type_of_donation = models.CharField(static.DONATION_TYPES, max_length=200)
    amount = models.PositiveIntegerField()
    prefix = models.CharField(max_length=10)
    receipt_serial_no = models.CharField(max_length=10)
    date_printing = models.DateField()
    print_indicator = models.CharField(max_length=1)
    void = models.BooleanField()
    converted=  models.BooleanField()
    name_of_fund = models.CharField(choices=static.FUND_NAMES, max_length=20)
    remarks = models.CharField(max_length=500)
    project = models.ForeignKey(to=Project)
    user = models.ForeignKey(to=DaySpringUser)
