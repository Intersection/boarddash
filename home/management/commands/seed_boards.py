from django.core.management.base import BaseCommand, CommandError
from django.db import connection


class Command(BaseCommand):
    help = 'Seeds the database with community board information'

    def handle(self, *args, **options):
        try:
            # Load data file
            # Remove all community boards
            # Add community boards from file
            self.stdout.write(self.style.SUCCESS('Successfully executed statements'))
        except Exception as e:
            self.stderr.write(e)
            self.stderr.write(self.style.ERROR('Could not execute statements'))

