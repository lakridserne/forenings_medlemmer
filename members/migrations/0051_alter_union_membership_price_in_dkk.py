# Generated by Django 4.2.2 on 2023-08-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0050_union_membership_price_in_dkk"),
    ]

    operations = [
        migrations.AlterField(
            model_name="union",
            name="membership_price_in_dkk",
            field=models.DecimalField(
                decimal_places=2,
                default=75,
                help_text="Medlemskabet skal koste minimum 75 kr. pga. Dansk Ungdoms Fællesråds medlemsdefinition.",
                max_digits=10,
                verbose_name="Pris for medlemskab",
            ),
        ),
    ]
