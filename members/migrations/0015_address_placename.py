# Generated by Django 2.2.8 on 2020-01-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0014_auto_20200103_2141"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="placename",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Stednavn"
            ),
        ),
    ]
