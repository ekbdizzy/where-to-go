import os
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import logging

logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):

    def handle(self, *args, **options):

        if os.path.exists('where_to_go/.env'):
            answer = input('File .env exists, type "yes" to overwrite it: ')
            if answer != 'yes':
                return

        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = get_random_string(50, chars)

        data = 'SECRET_KEY={}\n' \
               'DEBUG=False' \
               'ALLOWED_HOSTS=localhost'.format(secret_key)

        with open('where_to_go/.env', 'w') as file_object:
            file_object.write(data)

        logging.info('File .env created')
