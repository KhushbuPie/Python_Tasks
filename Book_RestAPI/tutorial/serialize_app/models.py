from django.db import models
from datetime import datetime

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     email = models.EmailField()
#     content = models.CharField(max_length=100)
#     created = models.DateField()

# class Comment:
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()



    