from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from .models import ChaletList, SelectChalet
from .forms import ReservationForm
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
        #chalet = ChaletList.objects.get(pk=chalet_id)
        chalet = get_object_or_404(queryset, pk=chalet_id)
        context = {
            'chalet': chalet,

        }
        return render(request, 'chalet_detail.html', context)


def reservation(view):
    '''show form to send reservation request'''
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form, }
    return render(request, 'reservation.html', context)
