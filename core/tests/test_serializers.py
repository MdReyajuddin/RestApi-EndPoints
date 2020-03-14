from django.test import TestCase

from ..factories import CompanyFactory
from ..serializers import CompanySerializer

class TestSerializer(TestCase):
    def test_model_field(self):
        company = CompanyFactory()

        for field_name in ['name', 'description', 'website', 'street_line1', 'street_line2', 'city', 'state', 'zip']:
            self.assertEqual(CompanySerializer.data['field_name'], getattr(company, field_name))