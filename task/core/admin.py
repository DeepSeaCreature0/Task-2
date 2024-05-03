from django.contrib import admin
from .models import Satellite, LaunchCountry

@admin.register(Satellite)
class SatelliteList(admin.ModelAdmin):
    list_display = (
        'object_name',
        'object_id',
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
        'mean_motion_ddot',
        'launch_country_name',
    )

    def launch_country_name(self, obj):
        return obj.launch_country.name if obj.launch_country else ''

@admin.register(LaunchCountry)
class LaunchCountryList(admin.ModelAdmin):
    list_display = (
        'name',
    )
