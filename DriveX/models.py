from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('renter', 'Renter'),
        ('owner', 'Car Owner'),
    )
    LICENSE_CHOICES = (
        ('two_wheeler', 'Two Wheeler'),
        ('four_wheeler', 'Four Wheeler'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='renter')
    
    # Personal Info
    address = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    
    # Documents
    aadhaar_number = models.CharField(max_length=20, blank=True)
    aadhaar_image = models.FileField(upload_to='documents/aadhaar/', blank=True, null=True)
    
    license_type = models.CharField(max_length=20, choices=LICENSE_CHOICES, blank=True)
    license_number = models.CharField(max_length=20, blank=True)
    license_image = models.FileField(upload_to='documents/license/', blank=True, null=True)
    
    is_verified = models.BooleanField(default=False)
    
    # Owner Specifics
    profile_photo = models.ImageField(upload_to='users/photos/', blank=True, null=True)
    payment_qr = models.ImageField(upload_to='users/qr/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
