from django.contrib import admin
from .models import ChaletOption, SelectChalet


@admin.register(ChaletOption)
class ChaletOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
