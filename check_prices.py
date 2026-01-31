import os
import django
import sys

# Setup Django environment
sys.path.append('d:\\DriveX')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DriveX.settings')
django.setup()

from Owner.models import Vehicle

print(f"{'ID':<5} {'Name':<30} {'Price per Day':<15} {'Type'}")
print("-" * 60)
for v in Vehicle.objects.all():
    print(f"{v.id:<5} {v.name:<30} {v.price_per_day} {type(v.price_per_day)}")
