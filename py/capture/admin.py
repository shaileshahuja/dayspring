from django.contrib import admin

# Register your models here.
from capture.models import Donation, DaySpringUser, DaySpringProject


class DonationAdmin(admin.ModelAdmin):
    model = Donation


class DaySpringUserAdmin(admin.ModelAdmin):
    model = DaySpringUser
    fields = ('first_name', 'last_name', 'email', 'salutation', 'birthday', 'address', 'postal_code', 'contact_no',
              'gender', 'id_type', 'id_no')

class DaySpringProjectAdmin(admin.ModelAdmin):
    model = DaySpringProject

admin.site.register(Donation, DonationAdmin)
admin.site.register(DaySpringUser, DaySpringUserAdmin)
admin.site.register(DaySpringProject, DaySpringProjectAdmin)