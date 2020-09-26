from django.core.management.base import BaseCommand
from places.models import Place, ImagesPlace
import requests
import logging
from utils import SaveImagePlace

logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            help='Create Place and ImagesPlace model with data from url'
        )

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url).json()
        title = response['title']
        imgs = response['imgs']
        description_short = response['description_short']
        description_long = response['description_long']
        coordinates_lng = response['coordinates']['lng']
        coordinates_lat = response['coordinates']['lat']

        place = Place.objects.get_or_create(
            title=title,
            description_short=description_short,
            description_long=description_long,
            coordinates_lng=coordinates_lng,
            coordinates_lat=coordinates_lat
        )

        if place[1]:
            logging.info('{} is created'.format(place[0].title))

        for image_link in imgs:
            s = SaveImagePlace(image_link)
            s.save()

            new_image_place = ImagesPlace.objects.create(
                place=place[0],
                image=s.media_path_to_image
            )
            new_image_place.save()
