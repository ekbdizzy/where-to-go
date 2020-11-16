import requests
from django.db import models
from django.urls import reverse
from django.core.files.base import ContentFile
from tinymce.models import HTMLField
import logging

logger = logging.getLogger('main')


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    detailed_description = HTMLField(blank=True, verbose_name='Подробная информация')
    longitude_coord = models.FloatField(default=0, verbose_name='Координаты долготы')
    latitude_coord = models.FloatField(default=0, verbose_name='Координаты широты')

    class Meta:
        verbose_name = 'Интересное место'
        verbose_name_plural = 'Интересные места'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_geojson(self):
        geo_json_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [self.longitude_coord, self.latitude_coord]
            },
            "properties": {
                "title": self.title,
                "placeId": self.id,
                "detailsUrl": reverse('place:detail', kwargs={"place_id": self.id})
            }
        }
        return geo_json_data


class PlacesImages(models.Model):

    @staticmethod
    def _get_image_data_from_url(url: str):
        response = requests.get(url)
        response.raise_for_status()
        return response.content

    def save_image_from_url(self, url):
        filename = url.split('/')[-1]
        self.image.save(name=filename,
                        content=ContentFile(self._get_image_data_from_url(url)))
        logger.info(f'{filename} is saved.')

    def get_path_to_places_image(self, filename: str) -> str:
        """Function is used in image.upload_to."""
        ext = filename.split(".")[-1]
        title = self.place.title
        filename = '.'.join([title, ext])
        return f'places/{title}/{filename}'

    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Название места')
    image = models.ImageField(upload_to=get_path_to_places_image, verbose_name='Файл с фотографией')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядковый номер', db_index=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ('order',)

    def __str__(self):
        return f"{self.id} {self.place.title}"
