# Generated by Django 4.2.11 on 2025-02-23 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0066_alter_person_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="name",
            field=models.CharField(
                max_length=200,
                validators=[
                    django.core.validators.RegexValidator(
                        '^(?!.*\\[:;,"[\\\\]{}*&^%$#@!\\_+=\\/\\])\\S+\\s+\\S+.*$',
                        inverse_match=True,
                        message="Indtast et gyldigt navn bestående af fornavn og minimum et efternavn.",
                    )
                ],
                verbose_name="Navn",
            ),
        ),
    ]
