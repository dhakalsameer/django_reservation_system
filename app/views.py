from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservationForm
from .models import Reservation

# Create your views here.
def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation successful!")

    reservations = Reservation.objects.all().order_by('-date_created')
    return render(request, 'index.html', {'form': form, 'reservations': reservations})
