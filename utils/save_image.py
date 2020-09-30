import os
import requests
from PIL import Image
from io import BytesIO
from typing import NoReturn
import logging

logger = logging.getLogger('main')


class SaveImagePlace:

    def __init__(self, url: str):

        if not os.path.exists('media'):
            os.mkdir('media')

        if not os.path.exists('media/places'):
            os.mkdir('media/places')

        self.url = url
        self.filename = url.split('/')[-1]
        self.media_path_to_image = 'places/{}'.format(self.filename)

    def save(self) -> NoReturn:
        """Get image from url and save to media/places/ folder."""

        response = requests.request(method='GET', url=self.url)
        image = Image.open(BytesIO(response.content))

        image.save('media/{}'.format(self.media_path_to_image))

        logger.info('{} is saved.'.format(self.media_path_to_image))
