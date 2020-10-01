import os
import requests
from PIL import Image
from io import BytesIO
from typing import NoReturn
import logging

logger = logging.getLogger('main')


class SaveImagePlace:

    def __init__(self):

        if not os.path.exists('media'):
            os.mkdir('media')

        if not os.path.exists('media/places'):
            os.mkdir('media/places')

    @staticmethod
    def _get_image_data_from_url(url: str):
        response = requests.get(url)
        response.raise_for_status()
        return response.content

    def save(self, url: str) -> NoReturn:
        """Save image to media/places/ folder."""
        image = Image.open(BytesIO(self._get_image_data_from_url(url)))
        filename = url.split('/')[-1]
        media_path_to_image = 'places/{}'.format(filename)
        image.save('media/{}'.format(media_path_to_image))
        logger.info('{} is saved.'.format(media_path_to_image))
