from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, View
from .models import ChaletList, SelectChalet
# from django.views.generic import View
# Create your views here.


def home(request):
    '''Shows homepage'''
    chalet_list = ChaletList.objects.all()
    context = {
        'chalet_list': chalet_list
    }
    return render(request, 'home.html', context)


class ChooseChalet(View):
    '''show selected chalet view'''
def get(self, request, route_id, *args, **kwargs):
    queryset = SelectChalet.objects.all()
    chalet = get_object_or_404(queryset, id=chalet_id)

    return render(request, 'description.html')
