# Generated by Django 4.2.3 on 2023-08-05 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]
