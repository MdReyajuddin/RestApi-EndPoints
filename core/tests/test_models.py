from django.test import TestCase

from ..models import Company
from ..factories import CompanyFactory

class TestCompanyName(TestCase):
    def str(self):
        company=CompanyFactory()
        self.assertEqual(str(company), company.name)
