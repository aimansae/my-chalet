from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ChaletList(models.Model):
    name = models.CharField(
        'Chalet Name', max_length=150, blank=False, unique=True)
    location = models.TextField(blank=False)
    image = CloudinaryField('Image', default='placeholder')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        '''Returns chalets name and relative price from ChaletList class'''
        return self.name


class SelectChalet(models.Model):
    name = models.ForeignKey(
        ChaletList, on_delete=models.CASCADE, blank=False, null=True, related_name='choose_chalet')
    location = models.ForeignKey(
        ChaletList, on_delete=models.CASCADE, blank=False, null=True, related_name='chalet_location')
    price = models.ForeignKey(
        ChaletList, on_delete=models.CASCADE, blank=False, null=True, related_name='chalet_price')
    description = models.TextField(blank=False)
    capacity = models.TextField(blank=False)
    selected_date = models.DateField(blank=False)
    chalet_images = CloudinaryField('Image', default='placeholder')
    request_reservation = models.ManyToManyField(
        User, related_name='send_interest', blank=True)

    def __str__(self):
        '''returns selected chalet and date'''
        return str(self.name) + ": $" + str(self.price)
