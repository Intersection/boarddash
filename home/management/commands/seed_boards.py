import csv

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.conf import settings

from home.models import CommunityBoard

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'boards.csv')

class Command(BaseCommand):
    help = 'Seeds the database with community board information'

    def handle(self, *args, **options):
        try:
            with open(filename) as f:
                for row in csv.DictReader(f, skipinitialspace=True):
                    model_record = CommunityBoard()
                    for key, value in row.items():
                        setattr(model_record, key, value)
                    model_record.save()
            self.stdout.write(self.style.SUCCESS('Successfully executed statements'))
        except Exception as e:
            self.stderr.write(e)
            self.stderr.write(self.style.ERROR('Could not execute statements'))

