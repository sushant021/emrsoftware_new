# Generated by Django 3.1.2 on 2020-11-25 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0006_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
    ]
