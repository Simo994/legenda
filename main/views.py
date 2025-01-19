from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import ReservationForm, UserRegisterForm, FeedbackForm
from .models import Reservation  # Import Reservation model
import logging
import json

logger = logging.getLogger(__name__)

def home(request):
    try:
        if request.method == 'POST' and 'feedback_form' in request.POST:
            logger.info("Processing feedback form submission")
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save()
                logger.info(f"Feedback saved successfully: {feedback.id}")
                return JsonResponse({'status': 'success'})
            else:
                logger.warning(f"Form validation failed: {form.errors}")
                return JsonResponse({
                    'status': 'error',
                    'errors': {
                        field: [str(error) for error in errors]
                        for field, errors in form.errors.items()
                    }
                })
        
        user_reservations = []
        if request.user.is_authenticated:
            user_reservations = Reservation.objects.filter(
                email=request.user.email,
                status='active'
            ).order_by('-date')
        
        feedback_form = FeedbackForm()
        return render(request, 'index.html', {
            'feedback_form': feedback_form,
            'user_reservations': user_reservations
        })
    except Exception as e:
        logger.error(f"Error in home view: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='login')
def reservation(request):
    try:
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.save()
                messages.success(request, 'Бронирование успешно создано!')
                return redirect('reservation_success')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'Ошибка в поле {field}: {error}')
        else:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email
            }
            form = ReservationForm(initial=initial_data)
        return render(request, 'reservation.html', {'form': form})
    except Exception as e:
        logger.error(f"Error in reservation view: {str(e)}")
        messages.error(request, 'Произошла ошибка при создании бронирования')
        return redirect('home')

@login_required(login_url='login')
def cancel_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
        if reservation.status == 'active':
            reservation.status = 'cancelled'
            reservation.save()
            messages.success(request, 'Бронирование успешно отменено')
        else:
            messages.warning(request, 'Это бронирование уже отменено')
        return redirect('home')
    except Reservation.DoesNotExist:
        messages.error(request, 'Бронирование не найдено')
        return redirect('home')

def reservation_success(request):
    return render(request, 'reservation_success.html')
