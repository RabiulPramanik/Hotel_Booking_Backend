# Generated by Django 5.0.6 on 2024-10-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_remove_bookingmodel_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='booking_type',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Upcoming', 'Upcoming'), ('Runing', 'Runing')], max_length=10, null=True),
        ),
    ]
