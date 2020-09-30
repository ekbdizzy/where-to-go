from django.core.management.base import BaseCommand
from places.models import Place, ImagesPlace
import requests
import logging
from utils import SaveImagePlace

import time

logger = logging.getLogger('main')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            help='Create Place and ImagesPlace model with data from url'
        )

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        if not response.ok:
            response.raise_for_status()

        response_data = response.json()
        title = response_data['title']
        imgs = response_data['imgs']
        description_short = response_data['description_short']
        description_long = response_data['description_long']
        coordinates_lng = response_data['coordinates']['lng']
        coordinates_lat = response_data['coordinates']['lat']

        place = Place.objects.get_or_create(
            title=title,
            description_short=description_short,
            description_long=description_long,
            coordinates_lng=coordinates_lng,
            coordinates_lat=coordinates_lat
        )

        if place[1]:
            logger.info('{} is created'.format(place[0].title))

        for image_link in imgs:
            s = SaveImagePlace(image_link)
            s.save()

            new_image_place = ImagesPlace.objects.create(
                place=place[0],
                image=s.media_path_to_image
            )
            new_image_place.save()
