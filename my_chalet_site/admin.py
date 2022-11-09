from django.contrib import admin
from .models import ChaletList, SelectChalet, MakeReservation


@admin.register(ChaletList)
class ChaletListAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(SelectChalet)
class SelectChaletAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'description',)

@admin.register(MakeReservation)
class MakeReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'capacity', 'date')