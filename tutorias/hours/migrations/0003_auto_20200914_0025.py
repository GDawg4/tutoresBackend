# Generated by Django 3.1 on 2020-09-14 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0002_auto_20200913_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hour',
            old_name='hour_start',
            new_name='hour',
        ),
    ]