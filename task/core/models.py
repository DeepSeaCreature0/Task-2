from django.db import models

class LaunchCountry(models.Model):
    name = models.CharField(max_length=100)

class Satellite(models.Model):
    object_name = models.CharField(max_length=100, verbose_name="OBJECT_NAME")
    object_id = models.CharField(max_length=20, verbose_name="OBJECT_ID")
    epoch = models.DateTimeField(verbose_name="EPOCH")
    mean_motion = models.FloatField(verbose_name="MEAN_MOTION")
    eccentricity = models.FloatField(verbose_name="ECCENTRICITY")
    inclination = models.FloatField(verbose_name="INCLINATION")
    ra_of_asc_node = models.FloatField(verbose_name="RA_OF_ASC_NODE")
    arg_of_pericenter = models.FloatField(verbose_name="ARG_OF_PERICENTER")
    mean_anomaly = models.FloatField(verbose_name="MEAN_ANOMALY")
    ephemeris_type = models.IntegerField(verbose_name="EPHEMERIS_TYPE")
    classification_type = models.CharField(max_length=10, verbose_name="CLASSIFICATION_TYPE")
    norad_cat_id = models.IntegerField(verbose_name="NORAD_CAT_ID")
    element_set_no = models.IntegerField(verbose_name="ELEMENT_SET_NO")
    rev_at_epoch = models.IntegerField(verbose_name="REV_AT_EPOCH")
    bstar = models.FloatField(verbose_name="BSTAR")
    mean_motion_dot = models.FloatField(verbose_name="MEAN_MOTION_DOT")
    mean_motion_ddot = models.FloatField(verbose_name="MEAN_MOTION_DDOT")
    launch_country = models.ForeignKey(LaunchCountry, on_delete=models.CASCADE)

    def __str__(self):
        return self.object_name
