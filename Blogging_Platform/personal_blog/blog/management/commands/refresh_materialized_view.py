from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Refresh materialized view for post with details'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('REFRESH MATERIALIZED VIEW post_with_details')