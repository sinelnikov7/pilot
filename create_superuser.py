import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auto_pilot.settings')
django.setup()
from django.contrib.auth.models import User

try:
    User.objects.create_superuser(username="admin", password="123",
                              is_superuser=True, is_staff=True)
except Exception:
    print("Суперюзер уже есть")