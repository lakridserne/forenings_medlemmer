# Generated by Django 3.2.13 on 2022-10-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0029_alter_activity_union"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="price_in_dkk",
            field=models.DecimalField(
                decimal_places=2,
                default=500,
                help_text="Hvis det er en sæsonaktivitet fratrækkes der automatisk 100 kr. til Coding Pirates Denmark pr. barn.",
                max_digits=10,
                verbose_name="Pris",
            ),
        ),
        migrations.AlterField(
            model_name="adminuserinformation",
            name="departments",
            field=models.ManyToManyField(
                blank=True, to="members.Department", verbose_name="Afdelinger"
            ),
        ),
        migrations.AlterField(
            model_name="adminuserinformation",
            name="unions",
            field=models.ManyToManyField(
                blank=True, to="members.Union", verbose_name="Foreninger"
            ),
        ),
        migrations.AlterField(
            model_name="emailitem",
            name="reciever",
            field=models.EmailField(max_length=254, verbose_name="Modtager"),
        ),
    ]
