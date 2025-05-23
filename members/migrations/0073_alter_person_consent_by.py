# Generated by Django 4.2.17 on 2025-04-13 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("members", "0072_alter_person_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="consent_by",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="person_consent_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Samtykke givet af",
            ),
        ),
    ]
