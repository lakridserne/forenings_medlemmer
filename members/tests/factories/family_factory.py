import factory
from factory import Faker, Maybe
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice
from members.models import Family
from members.tests.factories.factory_helpers import TIMEZONE


class FamilyFactory(DjangoModelFactory):
    class Meta:
        model = Family

    unique = Faker("uuid4")
    # email = Faker("email")
    email = factory.Sequence(
        lambda n: "family{0}@example.com".format(n)
    )  # Faker("email")
    # dont_send_mails = Faker("boolean")
    updated_at = Faker("date_time", tzinfo=TIMEZONE)
    confirmed_at = Faker("date_time", tzinfo=TIMEZONE)
    last_visit_at = Faker("date_time", tzinfo=TIMEZONE)
    anonymized_at = Maybe(
        FuzzyChoice([True, False]), Faker("date_time", tzinfo=TIMEZONE), None
    )
