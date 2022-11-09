from . models import MakeReservation
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model = MakeReservation
        fields = '__all__'
        
        