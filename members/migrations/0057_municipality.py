# Generated by Django 4.2.16 on 2024-10-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0056_alter_activityinvite_activity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Municipality",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "municipality",
                    models.CharField(max_length=255, verbose_name="Kommune"),
                ),
                ("address", models.CharField(max_length=255, verbose_name="Adresse")),
                ("zipcode", models.CharField(max_length=10, verbose_name="Postnr")),
                ("city", models.CharField(max_length=100, verbose_name="By")),
                ("email", models.EmailField(max_length=254, verbose_name="E-mail")),
            ],
            options={
                "verbose_name": "Kommune",
                "verbose_name_plural": "Kommuner",
                "ordering": ["municipality"],
            },
        ),
    ]
