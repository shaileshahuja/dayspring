from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

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

    def __unicode__(self):
        return self.first_name + ": " + self.email


class DaySpringProject(models.Model):
    name = models.CharField(choices=static.PROJECT_NAMES, max_length=200)

    def __unicode__(self):
        return self.name


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

    def __unicode__(self):
        return str(self.amount) + " by " + self.user.first_name


@receiver(post_save, sender=Donation)
def add(instance, sender, created, **kwargs):
    c = Combined()
    c.payment_type = instance.payment_type
    c.type_of_donation = instance.type_of_donation
    c.donation_date = instance.donation_date
    c.payment_number = instance.payment_number
    c.amount = instance.amount
    c.prefix = instance.prefix
    c.receipt_serial_no = instance.receipt_serial_no
    c.date_printing = instance.date_printing
    c.print_indicator = instance.print_indicator
    c.void = instance.void
    c.converted = instance.converted
    c.name_of_fund = instance.name_of_fund
    c.remarks = instance.remarks
    c.project_name = instance.project.name
    c.salutation = instance.user.salutation
    c.address = instance.user.address
    c.postal_code = instance.user.postal_code
    c.contact_no = instance.user.contact_no
    c.gender = instance.user.gender
    c.birthday = instance.user.birthday
    c.id_type = instance.user.id_type
    c.id_no = instance.user.id_no
    c.age = instance.user.age
    c.first_name = instance.user.first_name
    c.last_name = instance.user.last_name
    c.email = instance.user.email
    c.save()


class Combined(models.Model):
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
    project_name = models.CharField(choices=static.PROJECT_NAMES, max_length=200)
    salutation = models.CharField(choices=static.SALUTATIONS, max_length=5)
    address = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=6)
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(choices=static.GENDERS, max_length=10)
    birthday = models.DateField()
    id_type = models.CharField(choices=static.ID_TYPES, max_length=10)
    id_no = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
