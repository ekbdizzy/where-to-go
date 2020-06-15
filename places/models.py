from django.db import models


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


class ImagesPlace(models.Model):

    def upload_images_to_places(self, filename):
        filename = f'{self.place.title}.{filename.split(".")[-1]}'
        return f'places/{filename}'

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_images_to_places)

    def __str__(self):
        return f"{self.id} {self.place.title}"
