from django.core.management.base import BaseCommand
import requests
from datetime import datetime
from core.models import Satellite, LaunchCountry
from django.utils import timezone
import random
import csv

class Command(BaseCommand):
    help = 'Populate Satellites table with data from the JSON API and create a CSV file'

    def handle(self, *args, **kwargs):
        url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json'
        response = requests.get(url)
        data = response.json()

        countries = ['USA', 'Russia', 'China', 'India', 'France', 'Japan', 'UK', 'Germany', 'Italy', 'Canada']
        count = 0

        csv_file_path = 'satellites_data.csv'

        existing_countries = []
        for country_name in countries:
            country, created = LaunchCountry.objects.get_or_create(name=country_name)
            existing_countries.append(country)

        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = [
                'object_name', 'object_id', 'epoch', 'mean_motion', 'eccentricity', 'inclination',
                'ra_of_asc_node', 'arg_of_pericenter', 'mean_anomaly', 'ephemeris_type', 'classification_type',
                'norad_cat_id', 'element_set_no', 'rev_at_epoch', 'bstar', 'mean_motion_dot', 'mean_motion_ddot',
                'launch_country'
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for entry in data:
                
                if count == 600:
                    break

                epoch = timezone.make_aware(datetime.strptime(entry['EPOCH'], '%Y-%m-%dT%H:%M:%S.%f'))

                satellite = Satellite.objects.create(
                    object_name=entry['OBJECT_NAME'],
                    object_id=entry['OBJECT_ID'],
                    epoch=epoch,
                    mean_motion=entry['MEAN_MOTION'],
                    eccentricity=entry['ECCENTRICITY'],
                    inclination=entry['INCLINATION'],
                    ra_of_asc_node=entry['RA_OF_ASC_NODE'],
                    arg_of_pericenter=entry['ARG_OF_PERICENTER'],
                    mean_anomaly=entry['MEAN_ANOMALY'],
                    ephemeris_type=entry['EPHEMERIS_TYPE'],
                    classification_type=entry['CLASSIFICATION_TYPE'],
                    norad_cat_id=entry['NORAD_CAT_ID'],
                    element_set_no=entry['ELEMENT_SET_NO'],
                    rev_at_epoch=entry['REV_AT_EPOCH'],
                    bstar=entry['BSTAR'],
                    mean_motion_dot=entry['MEAN_MOTION_DOT'],
                    mean_motion_ddot=entry['MEAN_MOTION_DDOT'],
                    launch_country=random.choice(existing_countries) 
                )
                writer.writerow({
                    'object_name': satellite.object_name,
                    'object_id': satellite.object_id,
                    'epoch': satellite.epoch,
                    'mean_motion': satellite.mean_motion,
                    'eccentricity': satellite.eccentricity,
                    'inclination': satellite.inclination,
                    'ra_of_asc_node': satellite.ra_of_asc_node,
                    'arg_of_pericenter': satellite.arg_of_pericenter,
                    'mean_anomaly': satellite.mean_anomaly,
                    'ephemeris_type': satellite.ephemeris_type,
                    'classification_type': satellite.classification_type,
                    'norad_cat_id': satellite.norad_cat_id,
                    'element_set_no': satellite.element_set_no,
                    'rev_at_epoch': satellite.rev_at_epoch,
                    'bstar': satellite.bstar,
                    'mean_motion_dot': satellite.mean_motion_dot,
                    'mean_motion_ddot': satellite.mean_motion_ddot,
                    'launch_country': satellite.launch_country.name
                })
                count += 1

        self.stdout.write(self.style.SUCCESS('Satellites data populated successfully and CSV file created'))
