from django.db import models

class LaunchCountry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Satellite(models.Model):
    name = models.CharField(max_length=100,default="dummy")
    launch_country = models.ForeignKey(LaunchCountry, on_delete=models.CASCADE)
    norad_cat_id = models.IntegerField(unique=True,default=-1)

    def __str__(self):
        return self.name

class SatelliteData(models.Model):
    satellite = models.ForeignKey(Satellite, related_name='data', on_delete=models.CASCADE)
    epoch = models.DateTimeField()
    mean_motion = models.FloatField()
    eccentricity = models.FloatField()
    inclination = models.FloatField()
    ra_of_asc_node = models.FloatField()
    arg_of_pericenter = models.FloatField()
    mean_anomaly = models.FloatField()
    ephemeris_type = models.IntegerField()
    classification_type = models.CharField(max_length=10)
    norad_cat_id = models.IntegerField()
    element_set_no = models.IntegerField()
    rev_at_epoch = models.IntegerField()
    bstar = models.FloatField()
    mean_motion_dot = models.FloatField()
    mean_motion_ddot = models.FloatField()

    def __str__(self):
        return f"{self.satellite.name} - {self.epoch}"
