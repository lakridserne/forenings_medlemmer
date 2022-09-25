# Generated by Django 3.2 on 2022-09-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0027_alter_person_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='deleted_dtm',
        ),
        migrations.AddField(
            model_name='family',
            name='anonymized',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Anonymiseret'),
        ),
        migrations.AddField(
            model_name='person',
            name='anonymized',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Anonymiseret'),
        ),
    ]
