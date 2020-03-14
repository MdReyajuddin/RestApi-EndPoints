from factory import DjangoModelFactory, Faker

from core.models import Company

class CompanyFactory(DjangoModelFactory):
    name=Faker('company')
    description = Faker('text')
    website = Faker('url')
    street_line1 = Faker('street_address')
    city = Faker('city')
    state = Faker('state_abbr')
    zip = Faker('zip')

    class Meta:
        model = Company