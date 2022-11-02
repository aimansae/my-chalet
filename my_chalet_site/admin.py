from django.contrib import admin
from .models import ChaletList, SelectChalet


@admin.register(ChaletList)
class ChaletListAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(SelectChalet)
class SelectChaletAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'description',
                    'capacity', 'selected_date',)
