from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm

def index(request):
    return render(request, 'DriveX/index.html')

def auth_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        if 'login' in request.POST:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                selected_role = request.POST.get('role')
                
                # Role Check
                if hasattr(user, 'profile'):
                    # Allow Managers/Admins to bypass role check
                    if user.is_staff or user.profile.role == 'manager':
                        pass
                    elif user.profile.role != selected_role:
                        # Invalid Role - Force Logout
                        logout(request)
                        return render(request, 'DriveX/auth.html', {
                            'error': f"AUTH ERROR: Account is {user.profile.role}, but you tried to login as {selected_role}."
                        })

                login(request, user)
                return redirect('dashboard') # Logic redirected in dashboard_view
            else:
                # Form Invalid
                return render(request, 'DriveX/auth.html', {'login_form': form})

        elif 'register' in request.POST:
            form = UserRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('dashboard')
            else:
                 return render(request, 'DriveX/auth.html', {'register_form': form})
    
    return render(request, 'DriveX/auth.html')

@login_required
def dashboard_view(request):
    if request.user.is_staff:
        return redirect('Manager:dashboard')
    elif hasattr(request.user, 'profile'):
        if request.user.profile.role == 'owner':
            return redirect('Owner:dashboard')
        elif request.user.profile.role == 'renter':
            return redirect('Renter:dashboard')
    
    # Fallback
    return render(request, 'DriveX/dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('index')
