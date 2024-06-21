from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Create and refresh materialized view'

    def handle(self, *args, **kwargs):
        self.create_materialized_view()

    def create_materialized_view(self):
        sql_commands = [
            """
            CREATE TABLE IF NOT EXISTS post_with_details AS
            SELECT
                p.id AS post_id,
                p.title,
                p.body,
                p.created_on,
                p.last_modified,
                GROUP_CONCAT(c.name, ', ') AS category_names,
                GROUP_CONCAT(com.author || ': ' || com.body, '\n') AS comment_details
            FROM blog_post p
            LEFT JOIN blog_post_categories pc ON p.id = pc.post_id
            LEFT JOIN blog_category c ON pc.category_id = c.id
            LEFT JOIN blog_comment com ON p.id = com.post_id
            GROUP BY p.id
            """
        ]

  
