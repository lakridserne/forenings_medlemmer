from django.test import TestCase
from django.core.exceptions import ValidationError, PermissionDenied
from django.contrib.auth.models import User
from members.models.person import Person
from datetime import datetime, timedelta
from django.utils import timezone
from freezegun import freeze_time

from members.tests.factories import (
    PersonFactory,
    ActivityParticipantFactory,
    ActivityFactory,
)
from members.tests.factories.department_factory import DepartmentFactory
from members.tests.factories.factory_helpers import TIMEZONE
from members.tests.factories.waitinglist_factory import WaitingListFactory
from members.tests.factories.user_factory import UserFactory


class TestModelPerson(TestCase):
    def mock_reference_time(self, time):
        def mock(timezone):
            pass

        return mock

    def test_age_years(self):
        with freeze_time(datetime(2010, 3, 2)):
            person = PersonFactory(birthday=datetime(2000, 1, 1))
            self.assertEqual(person.age_years(), 10)

    def test_can_create_person(self):
        PersonFactory()  # no error should be thrown

    def test_saving_and_retrieving_persons(self):
        PersonFactory(name="Jane Doe", added_at=datetime(2018, 1, 1, tzinfo=TIMEZONE))
        PersonFactory(name="John Doe", added_at=datetime(2017, 1, 1, tzinfo=TIMEZONE))

        saved_persons = Person.objects.all()
        self.assertEqual(saved_persons.count(), 2)

        # retrieved in order of 'added' field
        self.assertEqual(saved_persons[0].name, "John Doe")
        self.assertEqual(saved_persons[1].name, "Jane Doe")

    def test_build_many(self):
        persons = PersonFactory.build_batch(size=20)
        self.assertEqual(len(persons), 20)
        self.assertEqual(Person.objects.count(), 0)
        self.assertFalse(Person.objects.exists())

    def test_creating_many(self):
        PersonFactory.create_batch(size=20)
        self.assertEqual(Person.objects.count(), 20)

    def test_firstname_allows_dash_in_names(self):
        person = PersonFactory(name="Hans-Christian Jensen Eriksen")
        self.assertEqual(person.firstname(), "Hans-Christian")

    def test_firstname_no_lastname(self):
        person = PersonFactory(name="Margrethe")
        self.assertEqual(person.firstname(), "Margrethe")

    def test_cannot_create_person_with_no_name(self):
        with self.assertRaises(ValidationError):
            person = PersonFactory(name="")
            person.full_clean()

    def test_cannot_change_person_to_unnamed(self):
        person = PersonFactory()
        with self.assertRaises(ValidationError):
            person.name = ""
            person.full_clean()

    def test_string_representation(self):
        person = PersonFactory()
        self.assertEqual(person.name, str(person))

    def test_defaults_to_parent(self):
        person = PersonFactory()
        self.assertEqual(person.membertype, Person.PARENT)

    def test_defaults_to_not_deleted(self):
        person = PersonFactory()
        self.assertEqual(person.deleted_dtm, None)

    def test_defaults_to_no_certificate(self):
        person = PersonFactory()
        self.assertEqual(person.has_certificate, None)

    def create_request_with_permission(self, permission):
        return type(
            "Request",
            (object,),
            {
                "user": type(
                    "User",
                    (object,),
                    {"has_perm": lambda self, perm: perm == permission},
                )()
            },
        )()

    def test_anonymize_person_in_single_member_family_no_permission(self):
        person = PersonFactory()

        request = self.create_request_with_permission("members.non_existing_permission")
        with self.assertRaises(PermissionDenied):
            person.anonymize(request)

    def test_anonymize_person_in_single_member_family_already_anonymized(self):
        person = PersonFactory(
            anonymized=True,
        )

        request = self.create_request_with_permission("members.anoymize_persons")
        with self.assertRaises(PermissionDenied):
            person.anonymize(request)

    def test_anonymize_person_in_single_member_family(self):
        person = PersonFactory()
        birthday = person.birthday
        municipality = person.municipality

        # create waiting list for person
        department = DepartmentFactory()
        WaitingListFactory(person=person, department=department)

        self.assertEqual(person.waitinglist_set.count(), 1)

        request = self.create_request_with_permission("members.anonymize_persons")
        person.anonymize(request)

        self.assertTrue(person.anonymized)
        self.assertEqual(person.name, "Anonymiseret")
        self.assertEqual(person.zipcode, "")
        self.assertEqual(person.municipality, municipality)  # should not be changed

        self.assertIsNotNone(person.birthday)

        # only day changes, not month or year
        self.assertEqual(person.birthday.year, birthday.year)
        self.assertEqual(person.birthday.month, birthday.month)
        self.assertNotEqual(person.birthday.day, birthday.day)

        # verify that person is removed from all waiting lists
        self.assertEqual(person.waitinglist_set.count(), 0)

        # given only one member of family, family should also be anonymized
        self.assertTrue(person.family.anonymized)

    def test_anonymize_single_person_in_multi_member_family(self):
        person_1 = PersonFactory()
        person_2 = PersonFactory(family=person_1.family)

        # create waiting list entries for both person
        department = DepartmentFactory()
        WaitingListFactory(person=person_1, department=department)
        WaitingListFactory(person=person_2, department=department)

        self.assertEqual(department.waitinglist_set.count(), 2)

        # sanity check that they are in the same family
        self.assertEqual(person_1.family, person_2.family)

        request = self.create_request_with_permission("members.anonymize_persons")
        person_1.anonymize(request)

        self.assertTrue(person_1.anonymized)
        self.assertFalse(person_2.anonymized)

        # verify that person_1 is removed from waiting list
        self.assertEqual(department.waitinglist_set.count(), 1)
        self.assertEqual(person_1.waitinglist_set.count(), 0)
        self.assertEqual(person_2.waitinglist_set.count(), 1)

        # given more than one member of family, family should not be anonymized
        self.assertFalse(person_1.family.anonymized)

    def test_anonymize_all_persons_in_multi_member_family(self):
        person_1 = PersonFactory()
        person_2 = PersonFactory(family=person_1.family)
        request = self.create_request_with_permission("members.anonymize_persons")

        # sanity check that are are pointing to same family object
        self.assertEqual(person_1.family, person_2.family)

        person_1.anonymize(request)

        self.assertTrue(person_1.anonymized)
        self.assertFalse(person_1.family.anonymized)  # not yet anonymized

        person_2.anonymize(request)

        self.assertTrue(person_2.anonymized)
        self.assertTrue(person_2.family.anonymized)

    def test_anonymize_person_with_user(self):
        person = PersonFactory()
        user = User.objects.create_user(
            username=person.name, email=person.email, password="password"
        )
        self.assertTrue(user.is_active)

        request = self.create_request_with_permission("members.anonymize_persons")
        person.anonymize(request)

        self.assertTrue(person.anonymized)

        # retrive updated user from database, and verify that user is no longer active
        user = User.objects.get(pk=user.pk)

        self.assertEqual(user.first_name, "Anonymiseret")
        self.assertNotEqual(user.email, person.email)  # email should be anonymized
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

    def test_anonymize_person_with_sent_emails(self):
        person = PersonFactory()
        email = person.emailitem_set.create(
            receiver=person.email, subject="Test email", body_text="Test email body"
        )

        request = self.create_request_with_permission("members.anonymize_persons")
        person.anonymize(request)

        self.assertTrue(person.anonymized)

        # retrieve updated email from database, and verify that email is anonymized
        email = person.emailitem_set.get(pk=email.pk)

        self.assertEqual(email.subject, "Anonymiseret")
        self.assertEqual(email.body_text, "")
        self.assertEqual(email.receiver, "")

    def test_is_anonymization_candidate_person_created_recently(self):
        """Person created less than 5 years ago should not be a candidate."""
        # Create person 3 years ago
        three_years_ago = timezone.now() - timedelta(days=3 * 365)
        with freeze_time(three_years_ago):
            person = PersonFactory()

        self.assertFalse(person.is_anonymization_candidate())

    def test_is_anonymization_candidate_recent_login(self):
        """Person with recent login should not be a candidate."""
        # Create person 6 years ago
        six_years_ago = timezone.now() - timedelta(days=6 * 365)
        with freeze_time(six_years_ago):
            person = PersonFactory()

        # Create user with recent login (2 years ago)
        user = UserFactory()
        user.last_login = timezone.now() - timedelta(days=2 * 365)
        user.save()
        person.user = user
        person.save()

        self.assertFalse(person.is_anonymization_candidate())

    def test_is_anonymization_candidate_recent_activity(self):
        """Person with recent activity participation should not be a candidate."""
        # Create person 6 years ago
        six_years_ago = timezone.now() - timedelta(days=6 * 365)
        with freeze_time(six_years_ago):
            person = PersonFactory()

        # Create activity that ended 2 years ago
        two_years_ago = timezone.now() - timedelta(days=2 * 365)
        activity = ActivityFactory(
            start_date=(two_years_ago - timedelta(days=30)).date(),
            end_date=two_years_ago.date(),
        )
        ActivityParticipantFactory(person=person, activity=activity)

        self.assertFalse(person.is_anonymization_candidate())

    def test_is_anonymization_candidate_old_person_no_recent_activity(self):
        """Person created long ago with no recent activity or login should be a candidate."""
        # Create person 6 years ago
        six_years_ago = timezone.now() - timedelta(days=6 * 365)
        with freeze_time(six_years_ago):
            person = PersonFactory()

        # Create old activity (7 years ago)
        seven_years_ago = timezone.now() - timedelta(days=7 * 365)
        activity = ActivityFactory(
            start_date=(seven_years_ago - timedelta(days=30)).date(),
            end_date=seven_years_ago.date(),
        )
        ActivityParticipantFactory(person=person, activity=activity)

        # Create user with old login (7 years ago)
        user = UserFactory()
        user.last_login = timezone.now() - timedelta(days=7 * 365)
        user.save()
        person.user = user
        person.save()

        self.assertTrue(person.is_anonymization_candidate())

    def test_is_anonymization_candidate_user_never_logged_in(self):
        """Person with user account that never logged in should be candidate if old enough."""
        # Create person 6 years ago
        six_years_ago = timezone.now() - timedelta(days=6 * 365)
        with freeze_time(six_years_ago):
            person = PersonFactory()

        # Create user with no login date
        user = UserFactory()
        user.last_login = None
        user.save()
        person.user = user
        person.save()

        self.assertTrue(person.is_anonymization_candidate())

    def test_is_anonymization_candidate_multiple_activities_latest_is_old(self):
        """Person with multiple activities where the latest is old should be a candidate."""
        # Create person 6 years ago
        six_years_ago = timezone.now() - timedelta(days=6 * 365)
        with freeze_time(six_years_ago):
            person = PersonFactory()

        # Create old activity (7 years ago)
        seven_years_ago = timezone.now() - timedelta(days=7 * 365)
        old_activity = ActivityFactory(
            start_date=(seven_years_ago - timedelta(days=30)).date(),
            end_date=seven_years_ago.date(),
        )
        ActivityParticipantFactory(person=person, activity=old_activity)

        # Create even older activity (8 years ago)
        eight_years_ago = timezone.now() - timedelta(days=8 * 365)
        older_activity = ActivityFactory(
            start_date=(eight_years_ago - timedelta(days=30)).date(),
            end_date=eight_years_ago.date(),
        )
        ActivityParticipantFactory(person=person, activity=older_activity)

        # Should be candidate because latest activity is still old
        self.assertTrue(person.is_anonymization_candidate())

    def test_is_anonymization_candidate_exactly_five_years(self):
        """Test edge case: person created exactly 5 years ago."""
        # Create person exactly 5 years ago
        exactly_five_years_ago = timezone.now() - timedelta(days=5 * 365)
        with freeze_time(exactly_five_years_ago):
            person = PersonFactory()

        # Should be candidate (created_at <= five_years_ago boundary)
        self.assertTrue(person.is_anonymization_candidate())
