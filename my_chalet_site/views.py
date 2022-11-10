from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from django.contrib import messages
from .models import *  # ChaletList, SelectChalet
from .forms import ReservationForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
# from django.views.generic import View
# Create your views here.


def home(request):
    '''Shows homepage'''
    chalet_list = ChaletList.objects.all()
    context = {
        'chalet_list': chalet_list
    }
    return render(request, 'home.html', context)


class ChaletDetail(View):
    '''show details about selected chalet'''

    def get(self, request, chalet_id, *args, **kwargs):
        queryset = SelectChalet.objects.all()
        # or chalet = ChaletList.objects.get(pk=chalet_id)
        chalet = get_object_or_404(queryset, pk=chalet_id)
        context = {
            'chalet': chalet,

        }
        return render(request, 'chalet_detail.html', context)


def reservation(request, chalet_id):

    chalet = SelectChalet.objects.get(pk=chalet_id)
    '''show form to make a reservation request'''
    form = ReservationForm()
    if request.method == 'POST':
        print('Testing', request.POST)
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ('Thank you, your reservation request is submitted!!'))
            return redirect('home') # need to craye a my booking page
    context = {'form': form,
               'chalet': chalet,
               }
    return render(request, 'reservation.html', context)
