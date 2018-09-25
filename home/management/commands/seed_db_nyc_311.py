import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.conf import settings

from home.models import NYC311Record, CommunityBoard


PAGE_SIZE = 30

def generate_slug(board_input_string):
    borough = board_input_string.split(' ')[1].lower()
    number = int(board_input_string.split(' ')[0])
    return '{}_{}'.format(borough, number)

def create_record(record):
    model_record = NYC311Record()
    slug = generate_slug(record['community_board'])
    try:
        board = CommunityBoard.objects.get(slug=slug)
    except:
        board = None

    for key, value in record.items():
        setattr(model_record, key, value)

    model_record.community_board_relation = board
    model_record.save()

def make_one_call(limit, offset):
    url_args = {
        'dataset_identifier': 'fhrw-4uyv',
        'format': 'json',
        'community_board': '01 BROOKLYN',
        'limit': limit,
        'offset': offset,
        'start_date': '2018-09-23T00:00:00.0000',
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
