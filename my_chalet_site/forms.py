from . models import MakeReservation
from django import forms
from django.forms import ModelForm

class ReservationForm(forms.ModelForm):
    class Meta:
        model = MakeReservation
        fields = 'fname','lname','phone','capacity','date'
        labels = {
            'email':'email',
            'lname': 'Last Name',
            'phone': 'Phone',
            'capacity':'Number of People',
            'date': 'Select Date',
            
        }
        