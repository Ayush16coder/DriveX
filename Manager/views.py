from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from DriveX.models import UserProfile
from Owner.models import Vehicle
from Renter.models import Booking
from django.db.models import Sum

def manager_login_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('Manager:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        passw = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            return render(request, 'Manager/login.html', {'error': f'Debug: User "{username}" not found.'})
            
        user = authenticate(request, username=username, password=passw)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('Manager:dashboard')
            else:
                return render(request, 'Manager/login.html', {'error': 'Access Denied: Account exists but is not Manager/Staff.'})
        else:
            return render(request, 'Manager/login.html', {'error': 'Debug: User found, but Password Incorrect.'})
            
    return render(request, 'Manager/login.html')

@staff_member_required
def dashboard(request):
    # Stats
    total_users = UserProfile.objects.count()
    active_users = UserProfile.objects.filter(user__is_active=True).count()
    inactive_users = total_users - active_users
    
    total_vehicles = Vehicle.objects.count()
    pending_vehicles_count = Vehicle.objects.filter(is_approved=False).count()
    
    revenue = Booking.objects.filter(status='completed').aggregate(Sum('total_price'))['total_price__sum'] or 0

    # Lists
    unverified_users = UserProfile.objects.filter(is_verified=False).exclude(user__is_staff=True)
    pending_vehicles = Vehicle.objects.filter(is_approved=False)

    # Full Management Lists
    all_users = UserProfile.objects.select_related('user').all().order_by('-user__date_joined')
    all_vehicles = Vehicle.objects.select_related('owner', 'owner__user').all().order_by('-is_approved')

    context = {
        'total_users': total_users,
        'active_users': active_users,
        'inactive_users': inactive_users, 
        'total_vehicles': total_vehicles,
        'pending_vehicles_count': pending_vehicles_count,
        'revenue': revenue,
        'unverified_users': unverified_users,
        'pending_vehicles': pending_vehicles,
        'all_users': all_users,
        'all_vehicles': all_vehicles,
        'action_items_count': unverified_users.count() + pending_vehicles_count,
    }
    return render(request, 'Manager/dashboard.html', context)

@staff_member_required
def verify_user(request, user_id):
    profile = get_object_or_404(UserProfile, id=user_id)
    profile.is_verified = True
    profile.save()
    return redirect('Manager:dashboard')

@staff_member_required
def reject_user(request, user_id):
    profile = get_object_or_404(UserProfile, id=user_id)
    profile.user.is_active = False # Deactivate login
    profile.user.save()
    return redirect('Manager:dashboard')

@staff_member_required
def approve_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.is_approved = True
    vehicle.save()
    return redirect('Manager:dashboard')

@staff_member_required
def reject_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.delete() # Or set flag
    return redirect('Manager:dashboard')
