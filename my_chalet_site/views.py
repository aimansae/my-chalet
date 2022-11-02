from django.shortcuts import render
from .models import ChaletOption, SelectChalet
# Create your views here.


def home(request):
    return render(request, 'home.html')