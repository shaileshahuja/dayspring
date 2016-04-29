import csv
import os

from datetime import date
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from django.conf import settings
from capture.models import DaySpringUser
from capture.models import Donation
from capture.models import DaySpringProject

class Command(BaseCommand):
    help = 'Creates a record'

    def add_arguments(self, parser):
        # parser.add_argument('-for', type=int, help='Create another loan request for the this borrower')
        # parser.add_argument('-status', type=int, help='The final status for an offer made for this loan request')
        # parser.add_argument('-lender', type=str, help='If specified with status, the lender makes an offer for this'
        #                                               'loan request that reaches the given status')
        pass

    def formatDate(self, date_str):

        if date_str == '':
            return "2000-12-12"

        date_split = date_str.split('/')

        year = date_split[2]
        month = date_split[0]
        day = date_split[1]

        return year + "-" + month + "-" + day

    def handle(self, *args, **options):
        #read file row by row
        with open(os.path.join(settings.DJANGO_DIR, 'capture/management/data/data.csv'), 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not DaySpringUser.objects.filter(id_no=row['ID No']).exists():
                    new_user = DaySpringUser()
                    #update info
                    new_user.address = row['Add 1']
                    new_user.first_name = split_names[0]
                    if len(split_names) > 1:
                        new_user.last_name = split_names[1]
                    else:
                        new_user.last_name = ""
                    new_user.postal_code = row['Postal Code']
                    new_user.email = row['Email Address']
                    new_user.contact_no = row['Tel No']
                    new_user.gender = row['Gender']
                    birthday = self.formatDate(row['Birthday'])
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

                    donation_date = self.formatDate(row['Date of Donation'])
                    new_donation.donation_date = parse_date(donation_date)

                    new_donation.prefix = row['Prefix']
                    new_donation.receipt_serial_no = row['Receipt Serial No']

                    printing_date = self.formatDate(row['Date of Printing'])
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
                    birthday = self.formatDate(row['Birthday'])
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

                    donation_date = self.formatDate(row['Date of Donation'])
                    new_donation.donation_date = parse_date(donation_date)

                    new_donation.prefix = row['Prefix']
                    new_donation.receipt_serial_no = row['Receipt Serial No']

                    printing_date = self.formatDate(row['Date of Printing'])
                    new_donation.date_printing = parse_date(printing_date)

                    new_donation.print_indicator = row['Print Indicator']
                    new_donation.void = True if row['Void'] == "Yes" else False
                    new_donation.converted = True if row['Converted'] == "Yes" else False
                    new_donation.name_of_fund = row['Name of Fund']
                    new_donation.remarks = row['Remarks']
                    new_donation.individual_indicator = True if row['Individual Indicator'] == "Yes" else False

                    new_donation.save()

        pass
