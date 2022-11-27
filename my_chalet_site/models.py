from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime, date, timedelta  # for date validation
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core import validators

CAPACITY = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'))


class ChaletList(models.Model):
    name = models.CharField(
        'Chalet Name', max_length=150, blank=False, unique=True)
    location = models.CharField(
        max_length=150, default='location', blank=False)
    image = CloudinaryField('Image', default='placeholder')
    description = models.TextField(default='description', blank=False)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    chalet_images = CloudinaryField('Image', default='placeholder')

    def __str__(self):
        '''Returns chalets name and relative price from ChaletList class'''
        return self.name


class MakeReservation(models.Model):
    def validation(date):
        if date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")
        elif date == timezone.now().date():
            raise ValidationError("Date cannot be today")

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None,
                             related_name='user_booking',)  # to remove null=True, default=None LATER

    selected_chalet = models.ForeignKey(
        ChaletList, on_delete=models.CASCADE, null=True)
    fname = models.CharField(
        'First Name', max_length=150, null=True, blank=False)
    lname = models.CharField(
        'Last Name', max_length=150, null=True, blank=False)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=False)
    capacity = models.CharField(
        max_length=2, choices=CAPACITY, default='2', blank=False)

    def date_tomorrow():
        now = timezone.now()
        return now + timedelta(days=1)

    # OR .date()+timedelta(days=1)
    date = models.DateField(default=date_tomorrow, validators=[validation])

    def __str__(self):
        '''returns selected chalet name'''
        return str(self.fname)
