from django.urls import path
from . import views

app_name = 'Manager'

urlpatterns = [
    path('login/', views.manager_login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('verify_user/<int:user_id>/', views.verify_user, name='verify_user'),
    path('reject_user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('approve_vehicle/<int:vehicle_id>/', views.approve_vehicle, name='approve_vehicle'),
    path('reject_vehicle/<int:vehicle_id>/', views.reject_vehicle, name='reject_vehicle'),
]
