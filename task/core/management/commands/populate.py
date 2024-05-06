import requests
from core.models import *
from django.core.management.base import BaseCommand
import csv
import os
import time
from datetime import datetime
from django.utils import timezone

CSV_FILE_PATH = 'satellite_data.csv'

def fetch_satellite_data(catnr):
    url = f"https://celestrak.org/NORAD/elements/gp.php?CATNR={catnr}&FORMAT=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

def add_data_to_csv(api_data):
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=api_data.keys())
            writer.writeheader()

    with open(CSV_FILE_PATH, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=api_data.keys())
        writer.writerow(api_data)

def update_satellite_data(catnr):
    api_data = fetch_satellite_data(catnr)

    if api_data:
        
        epoch = timezone.make_aware(datetime.strptime(api_data['EPOCH'], '%Y-%m-%dT%H:%M:%S.%f'))
        
        try:
            satellite=Satellite.objects.get(norad_cat_id=api_data['NORAD_CAT_ID'])
            check=True
        except Satellite.DoesNotExist:
            satellite=Satellite.objects.create(name=api_data['OBJECT_NAME'],
                                               launch_country=LaunchCountry.objects.order_by('?').first(),
                                               norad_cat_id=api_data['NORAD_CAT_ID'])
            check=False
        
        if check:
            last_satellite_data=SatelliteData.objects.filter(norad_cat_id=api_data['NORAD_CAT_ID']).latest('epoch')
            if last_satellite_data.epoch == epoch:
                add_data=False
            else:
                add_data=True
        else:
            add_data=True

        if add_data:

            SatelliteData.objects.create(
                satellite=satellite,
                epoch=epoch,
                mean_motion=api_data['MEAN_MOTION'],
                eccentricity=api_data['ECCENTRICITY'],
                inclination=api_data['INCLINATION'],
                ra_of_asc_node=api_data['RA_OF_ASC_NODE'],
                arg_of_pericenter=api_data['ARG_OF_PERICENTER'],
                mean_anomaly=api_data['MEAN_ANOMALY'],
                ephemeris_type=api_data['EPHEMERIS_TYPE'],
                classification_type=api_data['CLASSIFICATION_TYPE'],
                norad_cat_id=api_data['NORAD_CAT_ID'],
                element_set_no=api_data['ELEMENT_SET_NO'],
                rev_at_epoch=api_data['REV_AT_EPOCH'],
                bstar=api_data['BSTAR'],
                mean_motion_dot=api_data['MEAN_MOTION_DOT'],
                mean_motion_ddot=api_data['MEAN_MOTION_DDOT']
            )

            add_data_to_csv(api_data)


class Command(BaseCommand):
    help = 'Update satellite data from API'
    
    while(1):
        def handle(self, *args, **options):
            catnrs = [900,902,1361,1512,1520,2826,2866,2872,2874,2909]
            for catnr in catnrs:
                update_satellite_data(catnr)
        time.sleep(600)

