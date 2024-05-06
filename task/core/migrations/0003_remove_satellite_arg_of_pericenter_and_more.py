# Generated by Django 5.0.4 on 2024-05-06 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_satellite_arg_of_pericenter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satellite',
            name='arg_of_pericenter',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='bstar',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='classification_type',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='eccentricity',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='element_set_no',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='ephemeris_type',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='epoch',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='inclination',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='mean_anomaly',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='mean_motion',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='mean_motion_ddot',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='mean_motion_dot',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='norad_cat_id',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='object_name',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='ra_of_asc_node',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='rev_at_epoch',
        ),
        migrations.AddField(
            model_name='satellite',
            name='name',
            field=models.CharField(default='dummy', max_length=100),
        ),
        migrations.CreateModel(
            name='SatelliteData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoch', models.DateTimeField()),
                ('mean_motion', models.FloatField()),
                ('eccentricity', models.FloatField()),
                ('inclination', models.FloatField()),
                ('ra_of_asc_node', models.FloatField()),
                ('arg_of_pericenter', models.FloatField()),
                ('mean_anomaly', models.FloatField()),
                ('ephemeris_type', models.IntegerField()),
                ('classification_type', models.CharField(max_length=10)),
                ('norad_cat_id', models.IntegerField()),
                ('element_set_no', models.IntegerField()),
                ('rev_at_epoch', models.IntegerField()),
                ('bstar', models.FloatField()),
                ('mean_motion_dot', models.FloatField()),
                ('mean_motion_ddot', models.FloatField()),
                ('satellite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='core.satellite')),
            ],
        ),
    ]
