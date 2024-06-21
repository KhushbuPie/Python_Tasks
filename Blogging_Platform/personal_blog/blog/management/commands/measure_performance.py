from django.core.management.base import BaseCommand
from django.db import connection
from blog.models import Post, Category, Comment , PostWithDetails
import time

class Command(BaseCommand):
    help = 'Measure query performance with and without indexes'

    def handle(self, *args, **kwargs):
        self.measure_performance()

    def measure_performance(self):
        start_time = time.perf_counter()
        posts = Post.objects.select_related('categories','comments').all()
        end_time = time.perf_counter()
        print(f"Original query time: {end_time - start_time} seconds")

        start_time = time.perf_counter()
        posts = PostWithDetails.objects.all()
        end_time = time.perf_counter()
        print(f"Optimized query time : {end_time-start_time} seconds")

    # def measure_performance(self):
    #     queries = [
    #         "SELECT * FROM blog_post WHERE title LIKE 'Post%'",
    #         "SELECT * FROM blog_category WHERE name LIKE 'Category%'",
    #         "SELECT * FROM blog_comment WHERE author LIKE 'Author%'"
    #     ]

    #     for query in queries:
    #         # Drop indexes if they exist
    #         with connection.cursor() as cursor:
    #             cursor.execute(f"DROP INDEX IF EXISTS {self.get_index_name(query)}")

    #         # Measure query time without index
    #         start_time = time.perf_counter()
    #         with connection.cursor() as cursor:
    #             cursor.execute(query)
    #         end_time = time.perf_counter()
    #         print(f"Query Time Without Index: {end_time - start_time} seconds")

    #         # Create the index
    #         with connection.cursor() as cursor:
    #             cursor.execute(self.get_create_index_sql(query))

    #         # Measure query time with index
    #         start_time = time.perf_counter()
    #         with connection.cursor() as cursor:
    #             cursor.execute(query)
    #         end_time = time.perf_counter()
    #         print(f"Query Time With Index: {end_time - start_time} seconds")

    #         # Get and print query plans
    #         self.print_query_plan(query, with_index=False)
    #         self.print_query_plan(query, with_index=True)

    # def get_index_name(self, query):
    #     if 'blog_post' in query:
    #         return 'blog_post_title_idx'
    #     elif 'blog_category' in query:
    #         return 'blog_category_name_idx'
    #     elif 'blog_comment' in query:
    #         return 'blog_comment_author_idx'

    # def get_create_index_sql(self, query):
    #     if 'blog_post' in query:
    #         return "CREATE INDEX blog_post_title_idx ON blog_post (title)"
    #     elif 'blog_category' in query:
    #         return "CREATE INDEX blog_category_name_idx ON blog_category (name)"
    #     elif 'blog_comment' in query:
    #         return "CREATE INDEX blog_comment_author_idx ON blog_comment (author)"

    # def print_query_plan(self, query, with_index):
    #     index_status = 'WITH' if with_index else 'WITHOUT'
    #     print(f"Query Plan {index_status} Index:")
    #     with connection.cursor() as cursor:
    #         cursor.execute(f"EXPLAIN QUERY PLAN {query}")
    #         for row in cursor.fetchall():
    #             print(row)
