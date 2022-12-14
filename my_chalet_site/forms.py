from django.forms import ModelForm
from . models import MakeReservation
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from datetime import datetime, date, timedelta  # for date validation


class ReservationForm(forms.ModelForm):
    '''Reservation form class that shows form fields,
       with relative vidgets and labels'''

    phone = forms.IntegerField(widget=forms.NumberInput
                               (attrs={'placeholder': '00123456789'}),
                               )

    class Meta:
        model = MakeReservation
        fields = ('selected_chalet', 'fname', 'lname', 'email',
                  'phone', 'capacity', 'date')
        labels = {
            'selected_chalet': 'Selected Chalet',
            'email': 'Your Email',
            'lname': 'Last Name',
            'phone': 'Phone Nr',
            'capacity': 'Number of People',
            'date': 'Select Date',
        }

        widgets = {
            'selected_chalet': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['selected_chalet'].disable = True

    date = forms.DateField(
        widget=forms.SelectDateWidget(), initial=MakeReservation.date_tomorrow)
