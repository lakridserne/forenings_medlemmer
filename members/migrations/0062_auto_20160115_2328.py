# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import members.models
import members.models.activityinvite

class Migration(migrations.Migration):

    dependencies = [
        ('members', '0061_family_dont_send_mails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityinvite',
            name='expire_dtm',
            field=models.DateField(default=members.models.activityinvite._defaultInviteExpiretime, verbose_name='Udløber'),
        ),
    ]
