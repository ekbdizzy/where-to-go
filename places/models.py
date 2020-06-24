from django.db import models
from django.urls import reverse


class Place(models.Model):
    title = models.CharField(blank=True, null=True, default='', max_length=200)
    description_short = models.TextField(blank=True, null=True, default='')
    description_long = models.TextField(blank=True, null=True, default='')
    coordinates_lng = models.FloatField(blank=True, null=True, default=0)
    coordinates_lat = models.FloatField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.title

    def get_geojson(self):
        geo_json_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [self.coordinates_lng, self.coordinates_lat]
            },
            "properties": {
                "title": self.title,
                "placeId": self.id,
                "detailsUrl": reverse('place:detail', kwargs={"place_id": self.id})

            }
        }
        return geo_json_data


class ImagesPlace(models.Model):

    def upload_images_to_places(self, filename):
        filename = f'{self.place.title}.{filename.split(".")[-1]}'
        return f'places/{filename}'

    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_images_to_places)

    def __str__(self):
        return f"{self.id} {self.place.title}"
