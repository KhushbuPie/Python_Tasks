from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Category(models.Model):
    """Model representing a blog category."""
    """ Fields """
    name = models.CharField(max_length=30, unique=True ,validators=[RegexValidator(r'^[a-zA-Z\s]+$')])

    class Meta:
        verbose_name_plural ="Categories"
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name
    

class Post(models.Model):
    """Modek representing a blog post."""
    """ Fields """
    title = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z\s]+$')])
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    like = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['created_on']),
        ]
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    """Model representing a comment on a blog post."""
    """ Fields: """
    author = models.CharField(max_length=60, validators=[RegexValidator(r'^[a-zA-Z\s]+$')])
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")

    class Meta:
        indexes = [
            models.Index(fields=['author']),
            models.Index(fields=['created_on']),
        ]
    def __str__(self):
        return f"{self.author} on '{self.post}'"                    
    
class PostWithDetails(models.Model):
    """Denormalized model representing posts with details."""
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField()
    last_modified = models.DateTimeField()
    category_names = models.TextField()
    comment_details = models.TextField()

    class Meta:
        managed = False

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    is_active = models.BooleanField(default=True)