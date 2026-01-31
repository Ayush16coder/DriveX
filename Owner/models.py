from django.db import models
from DriveX.models import UserProfile

class Vehicle(models.Model):
    TYPE_CHOICES = (
        ('bike', 'Bike'),
        ('car', 'Car'),
    )
    FUEL_CHOICES = (
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
    )

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='vehicles')
    name = models.CharField(max_length=100) # Keep for display title
    vehicle_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='car')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, default='petrol')
    seating_capacity = models.IntegerField(default=4)
    
    model_year = models.IntegerField()
    license_plate = models.CharField(max_length=20)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)

    # Images / Docs
    image = models.ImageField(upload_to='vehicles/')
    rc_book = models.FileField(upload_to='vehicles/docs/', blank=True, null=True)
    insurance = models.FileField(upload_to='vehicles/docs/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.license_plate})"
