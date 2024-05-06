from django.core.management.base import BaseCommand
from core.models import *

class Command(BaseCommand):
    help = 'Populate LaunchCountry with dummy data'
    
    def handle(self, *args, **options):
        countries = ['USA', 'Russia', 'China', 'India', 'France', 'Japan', 'UK', 'Germany', 'Italy', 'Canada']

        for country in countries:
            LaunchCountry.objects.create(name=country)