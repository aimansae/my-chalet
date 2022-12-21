from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from .models import ChaletList, MakeReservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    '''Shows homepage with all the available chalets
    by rendering the home.html page
    '''

    chalet_list = ChaletList.objects.all()
    context = {
        'chalet_list': chalet_list,
    }
    return render(request, 'home.html', context)


class ChaletDetail(View):
    '''shows detailed desciption of the selected chalet'''

    def get(self, request, chalet_id, *args, **kwargs):

        queryset = ChaletList.objects.all()
        chalet = get_object_or_404(queryset, pk=chalet_id)
        context = {
            'chalet': chalet, }
        return render(request, 'chalet_detail.html', context)


def reservation(request, chalet_id):
    '''allows the user form to make a reservation request,
    first will show the selected chalet name and price
    '''

    chalet = ChaletList.objects.get(pk=chalet_id)
    name = ChaletList.name
    price = ChaletList.price
    form = ReservationForm(initial={'selected_chalet': chalet_id})
    user_reservation = chalet
  
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)

        if form.is_valid():
            reservation_form = form.save(commit=False)
            reservation_form.user = request.user
            reservation_form.save()
            messages.success(
                request, 'Thank you, your reservation request is submitted, we will contact you shortly!!')
            return redirect('my_reservations')
    else:
        form = ReservationForm(initial={'selected_chalet': chalet_id})

    context = {
        'form': form,
        'chalet': chalet,
        'name': name,
        'price': price,
        'user_reservation': user_reservation
    }
    return render(request, 'reservation.html', context)


def my_reservations(request):
    '''page that shows all the reservations the user made'''

    if request.user.is_authenticated:
        reservations = MakeReservation.objects.filter(user=request.user)
        user_reservation = MakeReservation.objects.all()

        context = {
            'reservations': reservations,
            'user_reservation': user_reservation,

        }
        return render(request, 'my_reservations.html', context)
    else:
        # if user is not authenticated:
        messages.warning(request, ('Please login to access this page'))
        return redirect('../accounts/signup')


@login_required
def edit_reservation(request, reservation_id):
    '''allows authenticated user to change reservation request.
    Can not modify the chalet, just the form input
    '''
    # if request.user.is_authenticated:
    reservations = get_object_or_404(
        MakeReservation, pk=reservation_id, user=request.user)

    form = ReservationForm(instance=reservations)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservations)
        if form.is_valid():
            form.save()
            messages.success(request, ('Reservation Updated'))
            return redirect('my_reservations')

    context = {'form': form,
               'reservations': reservations}

    return render(request, 'edit_reservation.html', context)

    # else:
    # if user is not authenticated:
    # messages.warning(request, ('Please login to access this page'))
    # return redirect('account_login')


@ login_required
def delete_reservation(request, reservation_id):
    '''allows the user to delete their reservation request'''

    # if request.user.is_authenticated:
    reservations = MakeReservation.objects.get(
        pk=reservation_id, user=request.user)
    reservations.delete()
    messages.warning(request, ('Reservation request deleted'))
    return redirect('my_reservations')
