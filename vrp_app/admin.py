# vrp_app/admin.py

from django.contrib import admin
from .models import Location, Vehicle

admin.site.register(Location)
admin.site.register(Vehicle)
