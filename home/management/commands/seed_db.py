from django.core.management.base import BaseCommand, CommandError
from django.db import connection


class Command(BaseCommand):
    help = 'Hits the 311 dataset and seeds the database'

    def handle(self, *args, **options):
        try:
            # Hit API here
            self.stdout.write(self.style.SUCCESS('Successfully executed statements'))
        except Exception as e:
            self.stderr.write(e)
            self.stderr.write(self.style.ERROR('Could not execute statements'))
