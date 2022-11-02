from django.contrib import admin
from .models import ChaletOption, SelectChalet


@admin.register(ChaletOption)
class ChaletOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(SelectChalet)
class SelectChaletAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'description',
                    'capacity', 'selected_date',)
