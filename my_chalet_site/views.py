from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from .models import ChaletList, MakeReservation  # SelectChalet
from .forms import ReservationForm
from django.contrib import messages

# from django.views.generic import View


def home(request):
    '''Shows homepage with all chalets available'''
    chalet_list = ChaletList.objects.all()
    context = {
        'chalet_list': chalet_list,
    }
    return render(request, 'home.html', context)


class ChaletDetail(View):
    '''shows detailed desciption of the selected chalet'''

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
    '''allows the user form to make a reservation request'''

    chalet = ChaletList.objects.get(pk=chalet_id)
    name = ChaletList.name
    price = ChaletList.price
# prima era cosi funzionava
    form = ReservationForm(initial={'selected_chalet': chalet_id})
    # form = ReservationForm()
    user_reservation = chalet

    if request.method == 'POST':
        form = ReservationForm(data=request.POST)

        if form.is_valid():
            reservation_form = form.save(commit=False)
            reservation_form.user = request.user
            reservation_form.save()
            messages.success(
                request, 'Thank you, your reservation request is submitted!!')
            return redirect('my_reservations')
    else:
        messages.error(
            request, 'The form is not valid'
        )
    # TO CHECK form = ReservationForm()
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
        messages.success(request, ('Please login to access this page'))
        return redirect('../accounts/signup')


def edit_reservation(request, reservation_id):
    if request.user.is_authenticated:
        # prima: reservations = MakeReservation.objects.get(pk=reservation_id)
        reservations = get_object_or_404(MakeReservation, pk=reservation_id)

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

    else:
        messages.success(request, ('Please log in to enter this page'))
        return redirect('accoount_login')


def delete_reservation(request, reservation_id):

    if request.user.is_authenticated:
        reservations = MakeReservation.objects.get(pk=reservation_id)
        reservations.delete()
        messages.success(request, ('Reservation request deleted'))
        return redirect('my_reservations')

