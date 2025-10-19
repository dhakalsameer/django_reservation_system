from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Reservation
from .forms import ReservationForm, RegisterForm
from django.http import HttpResponse


@login_required
def home(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'home.html', {'reservations': reservations})


@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'form.html', {'form': form})


@login_required
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    form = ReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form})


@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'reservation': reservation})


# --- AUTHENTICATION VIEWS ---

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def index(request):
    return render(request, 'index.html')

