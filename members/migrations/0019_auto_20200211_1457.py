# Generated by Django 2.2.9 on 2020-02-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0018_auto_20200130_1731"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="department_leaders",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"user__is_staff": True},
                to="members.Person",
            ),
        ),
    ]
