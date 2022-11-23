from . models import MakeReservation
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from datetime import datetime, date, timedelta  # for date validation


# for dateinput:

class DateInput(forms.DateInput):

    '''for date picker'''
    input_type = 'date'


class ReservationForm(forms.ModelForm):

    class Meta:
        model = MakeReservation
        fields = ('selected_chalet', 'fname', 'lname',
                  'phone', 'capacity', 'date',)
        labels = {
            'selected_chalet': 'selected_chalet',
            'email': 'email',
            'lname': 'Last Name',
            'phone': 'Phone',
            'capacity': 'Number of People',
            'date': 'Select Date',

        }

        # 'date': forms.DateInput(attrs={'type': 'date'}),

    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y',attrs={'type': 'date'}),
        #input_formats=('%d/%m/%Y', )

        )

    #selected_chalet = forms.ChoiceField(widget=forms.Select(attrs={'disabled':'disabled'}))
