from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# for date validation
from datetime import datetime, date, timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError

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
    # description = models.TextField(default='description', blank=False)
    image = CloudinaryField('Image', default='placeholder')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        '''Returns chalets name and relative price from ChaletList class'''
        return self.name


class SelectChalet(models.Model):
    name = models.ForeignKey(
        ChaletList, on_delete=models.CASCADE, blank=False, null=True, related_name='choose_chalet')
    location = models.CharField(
        max_length=150, default='location', blank=False)
    # make it float field models.FloatField
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField(default='description', blank=False)
    #selected_date = models.DateField()
    chalet_images = CloudinaryField('Image', default='placeholder')
    # request_reservation = models.ManyToManyField(
    # User, related_name='send_interest', blank=True)

    def __str__(self):
        '''returns selected chalet and date'''
        return str(self.name) + ": $" + str(self.price)


class MakeReservation(models.Model):
    # name = models.ForeignKey(
    # ChaletList, on_delete=models.CASCADE, blank=False, null=True,)
    # location = models.CharField(
    # max_length=150, default='location', blank=False)
    #price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    def validation(date):
        if date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")
        elif date==  timezone.now().date():
            raise ValidationError("Date cannot be today")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, default=None, related_name='user_booking',

    )  # to remove null=True, default=None LATER
    fname = models.CharField(
        'First Name', max_length=150, null=True, blank=False)
    lname = models.CharField(
        'Last Name', max_length=150, null=True, blank=False)
    email = models.EmailField(unique=True, null=True)
    phone = models.IntegerField(null=True, blank=False)
    capacity = models.CharField(
        max_length=2, choices=CAPACITY, default='2', blank=False)
    
    date = models.DateField(default=timezone.now()+timedelta(1), validators=[validation]) 
    #.date()+timedelta(days=1)


    def __str__(self):
        '''returns selected chalet name'''
        return str(self.name)
