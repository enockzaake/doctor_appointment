# Generated by Django 4.1.4 on 2022-12-31 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_doctor_customuser_is_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_doctor',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_patient',
        ),
    ]