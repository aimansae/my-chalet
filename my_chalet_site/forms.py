from django.forms import ModelForm
from . models import MakeReservation
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from datetime import datetime, date, timedelta  # for date validation



# for dateinput:

#class DateInput(forms.DateInput):

   # '''for date picker'''
   # input_type = 'date'


class ReservationForm(forms.ModelForm):

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

        # 'date': forms.DateInput(attrs={'type': 'date'})

    date = forms.DateField(
        widget=forms.SelectDateWidget(),initial=MakeReservation.date_tomorrow)
    
    
    
#dopo format era cosi attrs={'type': 'date'})