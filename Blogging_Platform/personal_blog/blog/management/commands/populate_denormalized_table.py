# from django.core.management.base import BaseCommand
# from django.db import connection

# class Command(BaseCommand):
#     help= 'Populate the denormalized PostWithDetails table' 

#     def handle(self, *args, **kwargs):
#         with connection/cursor() as cursor:
#             cursor.execute('''
#                 Insert INTO post_with_details (post_id, title, body, created_on, last_modified,category_names,comment_details)
#                 SELECT p.id,p.title, p.body, p.created_on, p.last_modified, 
#                         STRING_AGG(c.name, ', '),
#                         STRING_AGG(comm.author || ': ' || comm.body, '\n')
#                 FROM blog_post p
#                 LEFT JOIN blog_post_categories pc ON p.id = pc.post_id
#                 LEFT JOIN blog_category c ON pc.category_id = c.id
#                 LEFT JOIN blog_comment comm ON p.id = comm.post_id
#                 GROUP BY p.id 
#             ''')

# yourapp/management/commands/populate_denormalized_table.py
from django.core.management.base import BaseCommand
from django.db import connection
from blog.models import Post, PostWithDetails

class Command(BaseCommand):
    help = 'Populate the denormalized table PostWithDetails'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('DROP TABLE IF EXISTS post_with_details')
            cursor.execute('''
                CREATE TABLE post_with_details AS
                SELECT
                    p.id AS post_id,
                    p.title,
                    p.body,
                    p.created_on,
                    p.last_modified,
                    GROUP_CONCAT(c.name, ', ') AS category_names,
                    GROUP_CONCAT(co.author || ': ' || co.body, ', ') AS comment_details
                FROM
                    blog_post p
                LEFT JOIN
                    blog_post_categories pc ON p.id = pc.post_id
                LEFT JOIN
                    blog_category c ON c.id = pc.category_id
                LEFT JOIN
                    blog_comment co ON p.id = co.post_id
                GROUP BY
                    p.id
            ''')
        self.stdout.write(self.style.SUCCESS('Denormalized table populated successfully'))
