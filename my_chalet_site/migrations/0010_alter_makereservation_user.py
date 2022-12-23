# Generated by Django 4.1.3 on 2022-12-22 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_chalet_site', '0009_alter_makereservation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makereservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL),
        ),
    ]
