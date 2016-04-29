from django.contrib import admin

# Register your models here.
from capture.models import Donation, DaySpringUser, DaySpringProject


class DonationAdmin(admin.ModelAdmin):
    model = Donation


class DaySpringUserAdmin(admin.ModelAdmin):
    model = DaySpringUser


class DaySpringProjectAdmin(admin.ModelAdmin):
    model = DaySpringProject

admin.site.register(Donation, DonationAdmin)
admin.site.register(DaySpringUser, DaySpringUserAdmin)
admin.site.register(DaySpringProject, DaySpringProjectAdmin)