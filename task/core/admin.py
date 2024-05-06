from django.contrib import admin
from .models import LaunchCountry, Satellite, SatelliteData

admin.site.register(LaunchCountry)
admin.site.register(Satellite)
admin.site.register(SatelliteData)
