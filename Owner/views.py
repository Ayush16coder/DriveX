from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Vehicle
from .forms import VehicleForm, OwnerProfileForm, EditVehicleForm
from Renter.models import Booking
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def edit_profile(request):
    if request.user.profile.role != 'owner':
        return redirect('index')
    
    if request.method == 'POST':
        form = OwnerProfileForm(request.POST, request.FILES, instance=request.user.profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('Owner:dashboard')
    else:
        form = OwnerProfileForm(instance=request.user.profile, user=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'Owner/edit_profile.html', context)


@login_required
def dashboard(request):
    if request.user.profile.role != 'owner':
        return redirect('index')

    vehicles = Vehicle.objects.filter(owner=request.user.profile)
    
    # Booking Requests (All bookings for my vehicles)
    bookings = Booking.objects.filter(vehicle__in=vehicles).order_by('-created_at')
    
    # Earnings (Sum of confirmed/completed bookings)
    earnings = bookings.filter(status__in=['confirmed', 'completed']).aggregate(Sum('total_price'))['total_price__sum'] or 0

    # Handle Add Vehicle
    if request.method == 'POST' and 'add_vehicle' in request.POST:
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user.profile
            vehicle.save()
            return redirect('Owner:dashboard')

    context = {
        'user': request.user,
        'vehicles': vehicles,
        'bookings': bookings,
        'earnings': earnings
    }
    return render(request, 'DriveX/dashboard.html', context)

@login_required
def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    
    # Ensure ownership
    if vehicle.owner != request.user.profile:
        return redirect('Owner:dashboard')

    if request.method == 'POST':
        form = EditVehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('Owner:dashboard')
    else:
        form = EditVehicleForm(instance=vehicle)
    
    return render(request, 'Owner/edit_vehicle.html', {'form': form, 'vehicle': vehicle})

@login_required
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    
    # Ensure ownership
    
    if vehicle.owner == request.user.profile:
        vehicle.delete()
    
    return redirect('Owner:dashboard')

@login_required
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Ensure owner owns the vehicle
    if booking.vehicle.owner != request.user.profile:
        return redirect('Owner:dashboard')
        
    booking.status = 'confirmed'
    booking.save()
    return redirect('Owner:dashboard')

@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Ensure owner owns the vehicle
    if booking.vehicle.owner != request.user.profile:
        return redirect('Owner:dashboard')
        
    booking.status = 'cancelled'
    booking.save()
    return redirect('Owner:dashboard')
