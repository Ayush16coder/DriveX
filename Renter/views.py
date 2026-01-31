from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from Owner.models import Vehicle
from .forms import RenterProfileForm
from django.utils import timezone

@login_required
def edit_profile(request):
    if request.user.profile.role != 'renter':
        return redirect('index')
    
    if request.method == 'POST':
        form = RenterProfileForm(request.POST, request.FILES, instance=request.user.profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('Renter:dashboard')
    else:
        form = RenterProfileForm(instance=request.user.profile, user=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'Renter/edit_profile.html', context)


@login_required
def dashboard(request):
    if request.user.profile.role != 'renter':
        return redirect('index')
        
    bookings = Booking.objects.filter(renter=request.user.profile).order_by('-created_at')
    
    today = timezone.now().date()
    
    # Exclude vehicles that have an active 'confirmed' booking overlap
    booked_vehicle_ids = Booking.objects.filter(
        status='confirmed', 
        end_date__gte=today
    ).values_list('vehicle_id', flat=True)

    # Fetch Available Vehicles for Renters to Browse
    available_vehicles = Vehicle.objects.filter(
        is_available=True, 
        is_approved=True
    ).exclude(
        owner=request.user.profile
    ).exclude(
        id__in=booked_vehicle_ids
    )

    context = {
        'user': request.user,
        'bookings': bookings,
        'available_vehicles': available_vehicles
    }
    return render(request, 'DriveX/dashboard.html', context)

@login_required
def book_vehicle(request, vehicle_id):
    if request.method == 'POST':
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Calculate days (Naive calculation)
        from datetime import datetime
        d1 = datetime.strptime(start_date, "%Y-%m-%d")
        d2 = datetime.strptime(end_date, "%Y-%m-%d")
        days = abs((d2 - d1).days)
        if days == 0: days = 1 # Minimum 1 day
        
        total_price = days * vehicle.price_per_day
        
        booking = Booking.objects.create(
            renter=request.user.profile,
            vehicle=vehicle,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price,
            status='pending'
        )
        return redirect('Renter:dashboard')
    
        return redirect('Renter:dashboard')
    
    return redirect('Renter:dashboard')

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Ensure it's the renter's booking
    if booking.renter != request.user.profile:
        return redirect('Renter:dashboard')
        
    # Allow cancellation if pending or confirmed
    if booking.status in ['pending', 'confirmed']:
        booking.status = 'cancelled'
        booking.save()
        
    return redirect('Renter:dashboard')

@login_required
def booking_details(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Ensure it's the renter's booking
    if booking.renter != request.user.profile:
        return redirect('Renter:dashboard')
        
    return render(request, 'Renter/booking_details.html', {'booking': booking})
