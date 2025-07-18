from datetime import date, datetime
from django.test import TestCase
from members.models.person import Person

from .factories import UnionFactory
from .factories import DepartmentFactory
from .factories import FamilyFactory
from .factories import ActivityFactory
from .factories import MemberFactory


class TestModelMember(TestCase):
    def setUp(self):
        self.union = UnionFactory()
        self.department = DepartmentFactory(union=self.union)

        self.activity = ActivityFactory(
            start_date=date(datetime.now().year, 1, 1),
            end_date=date(datetime.now().year, 6, 1),
            department=self.department,
            union=self.union,
        )
        self.activity.save()

        self.family = FamilyFactory()
        self.family.save()

        self.person = Person(family=self.family, membertype=Person.CHILD)
        self.person.save()

    def test_can_create_member(self):
        MemberFactory()  # no errors should be thrown
