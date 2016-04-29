from django.contrib import admin

# Register your models here.
from capture.models import Donation


class DonationAdmin(admin.ModelAdmin):
    model = Donation

