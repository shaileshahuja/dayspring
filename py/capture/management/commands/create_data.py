from random import choice, randint

from django.core.management.base import BaseCommand
from faker import Factory

from capture.models import DaySpringProject, DaySpringUser, Donation
from py import static


class Command(BaseCommand):
    help = 'Creates a record'

    def add_arguments(self, parser):
        parser.add_argument('-limit', type=int, help='Number of records')
        # parser.add_argument('-status', type=int, help='The final status for an offer made for this loan request')
        # parser.add_argument('-lender', type=str, help='If specified with status, the lender makes an offer for this'
        #                                               'loan request that reaches the given status')
        pass

    @classmethod
    def generate_random_data(cls):
        faker = Factory.create()
        # Project
        data_dict = {
            "id_type": choice(static.ID_TYPES)[0],
            "id_no": randint(800000, 900000),
            "salutation": choice(static.SALUTATIONS)[0],
            "address": faker.address(),
            "gender": choice(static.GENDERS)[0],
            "postal_code": '6' + faker.postalcode(),
            "birthday": faker.date_time_between(start_date="-9y", end_date="-2y").date(),
            "contact_no": faker.phone_number(),
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email(),
            "password": "",
            "username": faker.email()
        }
        project_name = choice(static.PROJECT_NAMES)[0]
        p = DaySpringProject.objects.get_or_create(name=project_name)[0]
        if DaySpringUser.objects.filter(id_no=data_dict["id_no"]).exists():
            dpu = DaySpringUser.objects.get(id_no=data_dict["id_no"])
        else:
            dpu = DaySpringUser.objects.create(**data_dict)
        donation_dict = {
            "individual_indicator": faker.pybool(),
            "payment_type": choice(static.PAYMENT_TYPES)[0],
            "type_of_donation": choice(static.DONATION_TYPES)[0],
            "donation_date": faker.date_time_between(start_date="-5y", end_date="now").date(),
            "payment_number": str(faker.postalcode()),
            "amount": randint(1, 5000),
            "prefix": faker.pystr(max_chars=5),
            "receipt_serial_no": faker.pystr(max_chars=10),
            "date_printing": faker.date_time_between(start_date="-5y", end_date="now").date(),
            "print_indicator": faker.random_letter(),
            "void": faker.pybool(),
            "converted": faker.pybool(),
            "name_of_fund": choice(static.FUND_NAMES)[0],
            "project": p,
            "user": dpu
        }
        donation = Donation.objects.create(**donation_dict)

    def handle(self, *args, **options):
        for i in xrange(1000):
            self.generate_random_data()
