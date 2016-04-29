from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView, View
import os
import csv
from django.utils.dateparse import parse_date
from django.conf import settings
from django.views.generic.edit import FormView

from capture.models import DaySpringUser
from capture.models import Donation
from capture.models import DaySpringProject
from capture.forms import UploadFileForm


class HomePage(FormView):
    template_name = "upload.html"
    form_class = UploadFileForm
    success_url = 'capture/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(HomePage, self).form_valid(form)


def formatDate(date_str):
    if date_str == '':
        return "2000-12-12"

    date_split = date_str.split('/')

    year = date_split[2]
    month = date_split[0]
    day = date_split[1]

    return year + "-" + month + "-" + day


def parse_file(file):

    # read file row by row
    reader = csv.DictReader(file)
    for row in reader:
        if not DaySpringUser.objects.filter(id_no=row['ID No']).exists():
            new_user = DaySpringUser()
            # update info
            new_user.address = row['Add 1']
            split_names = row['Name'].split(" ")
            new_user.first_name = split_names[0]
            if len(split_names) > 1:
                new_user.last_name = split_names[1]
            else:
                new_user.last_name = ""
            new_user.postal_code = row['Postal Code']
            new_user.email = row['Email Address']
            new_user.contact_no = row['Tel No']
            new_user.gender = row['Gender']
            birthday = formatDate(row['Birthday'])
            new_user.birthday = parse_date(birthday)

            new_user.id_no = row['ID No']
            new_user.username = row['ID No']
            new_user.save()

            new_donation = Donation()
            new_donation.user = new_user

            new_project = DaySpringProject.objects.get_or_create(name=row['Project'])[0]
            new_donation.project = new_project
            new_donation.amount = int(row['Amount'])
            new_donation.type_of_donation = row['Type of Donation']
            new_donation.payment_type = row['Type of Payment']

            donation_date = formatDate(row['Date of Donation'])
            new_donation.donation_date = parse_date(donation_date)

            new_donation.prefix = row['Prefix']
            new_donation.receipt_serial_no = row['Receipt Serial No']

            printing_date = formatDate(row['Date of Printing'])
            new_donation.date_printing = parse_date(printing_date)

            new_donation.print_indicator = row['Print Indicator']
            new_donation.void = True if row['Void'] == "Yes" else False
            new_donation.converted = True if row['Converted'] == "Yes" else False
            new_donation.name_of_fund = row['Name of Fund']
            new_donation.remarks = row['Remarks']

            new_donation.individual_indicator = True if row['Individual Indicator'] == "Yes" else False

            new_donation.save()
        else:
            new_user = DaySpringUser.objects.get(id_no=row['ID No'])

            # update info
            new_user.address = row['Add 1']

            split_names = row['Name'].split(" ")
            new_user.first_name = split_names[0]
            if len(split_names) > 1:
                new_user.last_name = split_names[1]
            else:
                new_user.last_name = ""
            new_user.postal_code = row['Postal Code']
            new_user.email = row['Email Address']
            new_user.contact_no = row['Tel No']
            new_user.gender = row['Gender']
            birthday = formatDate(row['Birthday'])
            new_user.birthday = parse_date(birthday)

            new_user.id_no = row['ID No']
            new_user.username = row['ID No']

            new_user.save()
            new_donation = Donation()
            new_donation.user = new_user

            new_project = DaySpringProject.objects.get_or_create(name=row['Project'])[0]
            new_donation.project = new_project
            new_donation.amount = int(row['Amount'])
            new_donation.type_of_donation = row['Type of Donation']
            new_donation.payment_type = row['Type of Payment']

            donation_date = formatDate(row['Date of Donation'])
            new_donation.donation_date = parse_date(donation_date)

            new_donation.prefix = row['Prefix']
            new_donation.receipt_serial_no = row['Receipt Serial No']

            printing_date = formatDate(row['Date of Printing'])
            new_donation.date_printing = parse_date(printing_date)

            new_donation.print_indicator = row['Print Indicator']
            new_donation.void = True if row['Void'] == "Yes" else False
            new_donation.converted = True if row['Converted'] == "Yes" else False
            new_donation.name_of_fund = row['Name of Fund']
            new_donation.remarks = row['Remarks']
            new_donation.individual_indicator = True if row['Individual Indicator'] == "Yes" else False

            new_donation.save()


class UploadPage(View):
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            parse_file(request.FILES['file'])
            return HttpResponseRedirect('/capture/success')
