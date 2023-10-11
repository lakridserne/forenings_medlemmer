# Generated by Django 4.2 on 2023-09-24 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0043_alter_union_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="address",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="members.address",
                verbose_name="Adresse",
            ),
        ),
    ]
