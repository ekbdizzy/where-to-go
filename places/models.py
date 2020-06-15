from django.db import models


class Place(models.Model):
    title = models.CharField(blank=True, null=True, default='', max_length=200)
    description_short = models.TextField(blank=True, null=True, default='')
    description_long = models.TextField(blank=True, null=True, default='')
    coordinates_lng = models.FloatField(blank=True, null=True, default=0)
    coordinates_lat = models.FloatField(blank=True, null=True, default=0)
