"""
Vercel build script for Django static files
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command

# Collect static files
call_command('collectstatic', '--noinput', '--clear')
print("Static files collected successfully!")
