from django.contrib import admin
from .models import *

admin.site.register(LaunchCountry)
admin.site.register(Satellite)

@admin.register(SatelliteData)
class AdminSatelliteData(admin.ModelAdmin):
    list_display=(
        'satellite',
        'epoch',
        'mean_motion',
        'eccentricity',
        'inclination',
        'ra_of_asc_node',
        'arg_of_pericenter',
        'mean_anomaly',
        'ephemeris_type',
        'classification_type',
        'norad_cat_id',
        'element_set_no',
        'rev_at_epoch',
        'bstar',
        'mean_motion_dot',
        'mean_motion_ddot'
    )