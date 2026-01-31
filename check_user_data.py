
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from DriveX.models import UserProfile
from django.contrib.auth.models import User

print(f"{'Username':<15} | {'First Name':<15} | {'Last Name':<15} | {'Role':<10} | {'Aadhaar':<15}")
print("-" * 80)

for profile in UserProfile.objects.all():
    u = profile.user
    print(f"{u.username:<15} | {u.first_name:<15} | {u.last_name:<15} | {profile.role:<10} | {profile.aadhaar_number:<15}")
