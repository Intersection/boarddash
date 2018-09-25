import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.conf import settings

from home.models import BudgetRequest, CommunityBoard


PAGE_SIZE = 30
BOROUGHS = {
    '1': 'bronx',
    '2': 'brooklyn',
    '3': 'manhattan',
    '4': 'queens',
    '5': 'staten_island',
}

def generate_slug(boro, board):
    borough = BOROUGHS[boro]
    try:
        number = int(board)
    except:
        return None
    return '{}_{}'.format(borough, number)

def create_record(record):
    model_record = BudgetRequest()
    slug = generate_slug(record['boro'], record['board'])
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
        'dataset_identifier': 'jhkr-zj4k',
        'format': 'json',
        'limit': limit,
        'offset': offset,
    }
    url = "https://data.cityofnewyork.us/resource/{dataset_identifier}.{format}?$limit={limit}&$offset={offset}".format(**url_args)
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
