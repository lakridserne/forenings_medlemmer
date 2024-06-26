# Generated by Django 2.2.9 on 2020-02-03 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0018_auto_20200130_1731"),
    ]

    operations = [
        migrations.RenameField(
            model_name="union",
            old_name="cashier_email",
            new_name="cashier_email_old",
        ),
        migrations.RenameField(
            model_name="union",
            old_name="chairman_email",
            new_name="chairman_email_old",
        ),
        migrations.RenameField(
            model_name="union",
            old_name="second_chair_email",
            new_name="second_chair_email_old",
        ),
        migrations.RenameField(
            model_name="union",
            old_name="secratary_email",
            new_name="secretary_email_old",
        ),
        migrations.RenameField(
            model_name="union",
            old_name="cashier",
            new_name="cashier_old",
        ),
        migrations.RenameField(
            model_name="union",
            old_name="chairman",
            new_name="chairman_old",
        ),
        migrations.RenameField(
            model_name="union",
            old_name="second_chair",
            new_name="second_chair_old",
        ),
        migrations.RenameField(
            model_name="union",
            old_name="secretary",
            new_name="secretary_old",
        ),
        migrations.RenameField(
            model_name="union",
            old_name="boardMembers",
            new_name="boardMembers_old",
        ),
        migrations.AddField(
            model_name="union",
            name="boardMembers",
            field=models.ManyToManyField(blank=True, to="members.Person"),
        ),
        migrations.AddField(
            model_name="union",
            name="cashier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="cashier",
                to="members.Person",
            ),
        ),
        migrations.AddField(
            model_name="union",
            name="chairman",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="chairman",
                to="members.Person",
            ),
        ),
        migrations.AddField(
            model_name="union",
            name="second_chair",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="second_chair",
                to="members.Person",
            ),
        ),
        migrations.AddField(
            model_name="union",
            name="secretary",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="secretary",
                to="members.Person",
            ),
        ),
    ]
