# Generated by Django 3.1 on 2020-08-30 05:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200829_2204'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutors', '0003_auto_20200811_1611'),
    ]