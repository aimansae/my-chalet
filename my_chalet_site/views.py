from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from django.contrib import messages
from .models import ChaletList, MakeReservation  # SelectChalet
from .forms import ReservationForm
# from django.views.generic import View


def home(request):
    '''Shows homepage with all chalets available'''
    chalet_list = ChaletList.objects.all()
    context = {
        'chalet_list': chalet_list,
    }
    return render(request, 'home.html', context)


class ChaletDetail(View):
    '''show details about selected chalet'''

    def get(self, request, chalet_id, *args, **kwargs):
        # questo era gia cosi
        # queryset = SelectChalet.objects.all()
        # aggiunto dopo
        queryset = ChaletList.objects.all()
        # or chalet = ChaletList.objects.get(pk=chalet_id)
        chalet = get_object_or_404(queryset, pk=chalet_id)
        context = {
            'chalet': chalet, }
        return render(request, 'chalet_detail.html', context)


def reservation(request, chalet_id):
    '''show form to make a reservation request'''
# pima wea cosi:
    chalet = ChaletList.objects.get(pk=chalet_id)
    
    form = ReservationForm(initial={'selected_chalet':chalet_id})

    if request.method == 'POST':
        form = ReservationForm(data=request.POST)

        if form.is_valid():
            reservation_form = form.save(commit=False)
            reservation_form.user = request.user
            # to delete form.instance.name = request.user.username
            reservation_form.save()
            messages.success(
                request, 'Thank you, your reservation request is submitted!!')
            # need to create a my booking page
            return redirect('my_reservations')
    else:
        messages.error(
            request, 'The form is not valid'
        )
    #form = ReservationForm()
    context = {
        'form': form,
        'chalet': chalet
    }
    return render(request, 'reservation.html', context)


def my_reservations(request):
    chalet = ChaletList.objects.all()

    if request.user.is_authenticated:

        reservations = MakeReservation.objects.filter(user=request.user)
        context = {
            'reservations': reservations,
            'chalet':chalet,

        }
        return render(request, 'my_reservations.html', context)
    else:
        # if user is not authenticated:
        messages.success(request, ('Please login to access this page'))
        return redirect('../accounts/signup')


#def edit_reservation(request, chalet_id):

    #chalet = get_object_or_404(ChaletList, pk=chalet_id)
    #if request.method == 'POST':
        #form = ReservationForm(request.POST, instance=chalet)
        #if form.is_valid():
            #form.save()
            #messages.success(request, 'Reservation updated!')
            #return redirect('my_reservations')

    #context = {
        #'form': form,
        #'chalet': chalet
    #}

    #return reder(request, 'edit_reservation.html', context)
