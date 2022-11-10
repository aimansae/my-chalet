from . models import MakeReservation
from django import forms
from django.forms import ModelForm
#from bootstrap_datepicker_plus import DatePickerInput


# for dateinput:

class DateInput(forms.DateInput):

    '''for date picker'''
    input_type = 'date'


class ReservationForm(ModelForm):
    class Meta:
        model = MakeReservation
        fields = '__all__'  # 'fname', 'lname', 'phone', 'capacity' date,
        labels = {
            'email': 'email',
            'lname': 'Last Name',
            'phone': 'Phone',
            'capacity': 'Number of People',
            'date': 'Select Date',

        }
        widgets = {
            'date': DateInput()#format = '%d-%m-%Y',attrs={'type': 'date'}),
        }
        
        
