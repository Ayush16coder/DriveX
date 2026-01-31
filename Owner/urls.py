from django.urls import path
from . import views

app_name = 'Owner'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('vehicle/edit/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicle/delete/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
    path('booking/accept/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('booking/reject/<int:booking_id>/', views.reject_booking, name='reject_booking'),
]
