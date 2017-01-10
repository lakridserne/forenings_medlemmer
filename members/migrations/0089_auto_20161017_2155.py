# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-17 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0088_auto_20161016_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dtm', models.DateTimeField(auto_now_add=True, verbose_name='Oprettet')),
                ('title', models.CharField(max_length=200, verbose_name='Titel')),
                ('count', models.IntegerField(default=1, verbose_name='Antal enheder')),
                ('link', models.URLField(blank=True, verbose_name='Link til mere info')),
                ('notes', models.TextField(blank=True, verbose_name='Generelle noter')),
                ('buy_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Købs pris')),
                ('buy_place', models.TextField(blank=True, null=True, verbose_name='Købs sted')),
                ('buy_date', models.DateField(blank=True, null=True, verbose_name='Købs dato')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Department')),
            ],
            options={
                'verbose_name': 'Udstyr',
                'verbose_name_plural': 'Udstyr',
            },
        ),
        migrations.CreateModel(
            name='EquipmentLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='Antal enheder udlånt')),
                ('loaned_dtm', models.DateField(auto_now_add=True, verbose_name='Udlånt')),
                ('expected_back_dtm', models.DateField(blank=True, null=True, verbose_name='Forventet returneret')),
                ('returned_dtm', models.DateField(blank=True, null=True, verbose_name='Afleveret')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Noter')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Department')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Equipment')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Person')),
            ],
            options={
                'verbose_name': 'Udstyrs udlån',
                'verbose_name_plural': 'Udstyrs udlån',
            },
        ),
        migrations.AlterField(
            model_name='union',
            name='founded',
            field=models.DateField(blank=True, null=True, verbose_name='Stiftet'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='union',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Union'),
        ),
    ]