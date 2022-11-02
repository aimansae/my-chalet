from django.shortcuts import render
from .models import ChaletList, SelectChalet
# Create your views here.


def home(request):
    '''Shows homepage'''
    chalet_list = ChaletList.objects.all()
    context = {
        'chalet_list': chalet_list
    }
    return render(request, 'home.html', context)
