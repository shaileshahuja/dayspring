
from random import choice, randint

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from faker import Factory
from rest_framework.test import APIClient

from borrower.models import BorrowerProfile
from main import static
from main.static import JOB_TYPE, OCCUPATION_CHOICES, GENDER, CITIZENSHIP, WORKPASS, \
    HOUSING_OWNERSHIP, PROPERTY_TYPE, YES_NO, BORROWER_LOAN_PERIODS, EMPLOYMENT_LENGTHS, PURPOSE


class Command(BaseCommand):
    help = 'Creates a record'

    def add_arguments(self, parser):
        # parser.add_argument('-for', type=int, help='Create another loan request for the this borrower')
        # parser.add_argument('-status', type=int, help='The final status for an offer made for this loan request')
        # parser.add_argument('-lender', type=str, help='If specified with status, the lender makes an offer for this'
        #                                               'loan request that reaches the given status')
        pass
    
    @classmethod
    def generate_random_data(cls):
        faker = Factory.create()
        email = faker.email()
        monthly_income = randint(1000, 2000)

        data_dict = {
            "email": email,
            "password": email[:30],
            "job_type": choice(JOB_TYPE)[0],
            "occupation": choice(OCCUPATION_CHOICES)[0],
            "gender": choice(GENDER)[0],
            "age": randint(18, 99),
            "citizenship": choice(CITIZENSHIP)[0],
            "work_pass": choice(WORKPASS)[0],
            "work_pass_expiry": faker.date_time_between(start_date="now", end_date="+2y").date(),
            "housing_ownership": choice(HOUSING_OWNERSHIP)[0],
            "property_type": choice(PROPERTY_TYPE)[0],
            "outstanding_ml_balance": randint(1, 1000),
            "ml_count": randint(1, 10),
            "outstanding_bank_loan": randint(1, 2000),
            "any_outstanding_cc_debt": choice(YES_NO)[0],
            "outstanding_cc_debt": randint(1, 2000),
            "declared_bankrupt": choice(YES_NO)[0],
            "referrer": faker.first_name(),
            "current_url": faker.first_name(),
            "monthly_income": monthly_income,
            "loan_amount": randint(monthly_income, monthly_income + 1000),
            "preferred_payment_period": randint(1, 12),
            "preferred_type": choice(BORROWER_LOAN_PERIODS)[0],
            "purpose": choice(PURPOSE)[0],
            'any_outstanding_bank_loan': choice(YES_NO)[0],
            'length_of_emp': choice(EMPLOYMENT_LENGTHS)[0],
            'user_discharged': choice(YES_NO)[0],
            'postal_code': "123456",
            'occupation_other': "other"
        }

        return data_dict

    def handle(self, *args, **options):
        client = APIClient()
        data_dict = self.generate_random_data()
        if options["for"]:
            borrower = BorrowerProfile.objects.get(pk=options["for"])
            client.force_authenticate(borrower.user)
            response = client.post(reverse('api-v1:borrower_create_loan_request'), data_dict, format='json')
            loan_request = borrower.active_loan_request
        else:
            response = client.post(reverse('api-v1:borrower_signup'), data_dict, format='json')
            borrower = BorrowerProfile.objects.get(user__email=data_dict["email"])
            loan_request = borrower.active_loan_request
        if options["status"]:
            loan_request = borrower.active_loan_request
            args = ["-for", str(loan_request.id)]
            if options["lender"]:
                args += ["-lender", str(options["lender"])]
            call_command("create_lender_offer", *args)
            call_command("alter_loan_request", str(loan_request.id), "-status", str(options["status"]))
        self.stdout.write(str(loan_request.id))
        self.stdout.write(borrower.user.email)
