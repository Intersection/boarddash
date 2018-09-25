import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.conf import settings

from home.models import NYC311Record


PAGE_SIZE = 30

def create_record(record):
    model_record = NYC311Record()
    for key, value in record.items():
        setattr(model_record, key, value)
    model_record.save()

def make_one_call(limit, offset):
    url_args = {
        'dataset_identifier': 'fhrw-4uyv',
        'format': 'json',
        'community_board': '01 MANHATTAN',
        'limit': limit,
        'offset': offset,
        'start_date': '2018-09-21T00:00:00.0000',
    }
    url = "https://data.cityofnewyork.us/resource/{dataset_identifier}.{format}?community_board={community_board}&$limit={limit}&$offset={offset}&$order=:id&$where=created_date > '{start_date}'".format(**url_args)
    return requests.get(url, timeout=settings.REQUESTS_TIMEOUT_SECONDS)

def process_one_call(response_data):
    for record in response_data:
        create_record(record)

class Command(BaseCommand):
    help = 'Hits the 311 dataset and seeds the database'

    def handle(self, *args, **options):
        try:
            offset = 0
            records_in_call = PAGE_SIZE
            while records_in_call == PAGE_SIZE:
                response = make_one_call(PAGE_SIZE, offset)
                records_in_call = len(response.json())
                process_one_call(response.json())
                offset += PAGE_SIZE

            self.stdout.write(self.style.SUCCESS('Successfully executed statements'))
        except Exception as e:
            self.stderr.write(e)
            self.stderr.write(self.style.ERROR('Could not execute statements'))