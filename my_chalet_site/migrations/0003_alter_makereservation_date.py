# Generated by Django 4.1.3 on 2022-11-22 12:03

from django.db import migrations, models
import my_chalet_site.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_chalet_site', '0002_alter_makereservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makereservation',
            name='date',
            field=models.DateTimeField(default=my_chalet_site.models.MakeReservation.date_tomorrow),
        ),
    ]