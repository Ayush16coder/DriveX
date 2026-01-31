from django.urls import path
from . import views

app_name = 'Renter'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('book/<int:vehicle_id>/', views.book_vehicle, name='book_vehicle'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('booking/details/<int:booking_id>/', views.booking_details, name='booking_details'),
]
