from django.contrib import admin
from .models import ChaletList, MakeReservation


@admin.register(ChaletList)
class ChaletListAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(MakeReservation)
class MakeReservationAdmin(admin.ModelAdmin):
    list_display = ('fname', 'capacity', 'date')
