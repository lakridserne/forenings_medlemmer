# Generated by Django 4.2.2 on 2023-08-20 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0048_alter_activity_price_in_dkk_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="member",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="members.member",
            ),
        ),
    ]
