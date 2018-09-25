import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.conf import settings

from home.models import NYC311Record


class Command(BaseCommand):
    help = 'Hits the 311 dataset and seeds the database'

    def handle(self, *args, **options):
        try:
            url_args = {
                'dataset_identifier': 'fhrw-4uyv',
                'format': 'json',
                'community_board': '01 MANHATTAN',
                'limit': 2,
                'offset': 14100,
            }
            url = "https://data.cityofnewyork.us/resource/{dataset_identifier}.{format}?community_board={community_board}&$limit={limit}&$offset={offset}&$order=:id&$where=created_date > '2018-01-01T00:00:00.0000'".format(**url_args)
            response = requests.get(url, timeout=settings.REQUESTS_TIMEOUT_SECONDS)

            for record in response.json():
                print('RECORD')
                print(record)
                # Create 311Record object here
                #NYC311Record.objects.create(**record)
                model_record = NYC311Record()
                for key, value in record.items():
                    setattr(model_record, key, value)
                model_record.save()
            self.stdout.write(self.style.SUCCESS('Successfully executed statements'))
        except Exception as e:
            self.stderr.write(e)
            self.stderr.write(self.style.ERROR('Could not execute statements'))
