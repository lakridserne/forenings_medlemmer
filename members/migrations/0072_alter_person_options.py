# Generated by Django 4.2.17 on 2025-04-13 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0071_consent"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="person",
            options={
                "ordering": ["added_at"],
                "permissions": (
                    (
                        "view_full_address",
                        "Can view persons full address + phonenumber + email",
                    ),
                    ("view_all_persons", "Can view persons not related to department"),
                    ("anonymize_persons", "Can anonymize persons"),
                    (
                        "view_consent_information",
                        "Can view consent information for persons",
                    ),
                ),
                "verbose_name": "Person",
                "verbose_name_plural": "Personer",
            },
        ),
    ]
