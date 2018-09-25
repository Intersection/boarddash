import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.conf import settings


class Command(BaseCommand):
    help = 'Hits the 311 dataset and seeds the database'

    def handle(self, *args, **options):
        try:
            url_args = {
                'dataset_identifier': 'fhrw-4uyv',
                'format': 'json',
                'community_board': '01 MANHATTAN',
            }
            url = "https://data.cityofnewyork.us/resource/{dataset_identifier}.{format}?community_board={community_board}&$limit=2&$offset=14100&$order=:id&$where=created_date > '2018-01-01T00:00:00.0000'".format(**url_args)
            response = requests.get(url, timeout=settings.REQUESTS_TIMEOUT_SECONDS)
            print(response.json())
            self.stdout.write(self.style.SUCCESS('Successfully executed statements'))
        except Exception as e:
            self.stderr.write(e)
            self.stderr.write(self.style.ERROR('Could not execute statements'))
