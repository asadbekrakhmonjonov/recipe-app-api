import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError

""" Django command for the database to be available. """

class Command(BaseCommand):
    """ Django command to wait for the database to be available. """

    def handle(self, *args, **options):
        """ Entrypoint for command """
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, one sec ....')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
