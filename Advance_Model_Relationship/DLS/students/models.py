from django.db import models

# Create your models here.

class subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

class student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)

class Passport(models.Model):
    passport_id = models.BigAutoField(primary_key=True)
    passport_no = models.CharField(max_length=10)

    def __str__(self):
        return self.passport_no
    
class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address= models.TextField()
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def apply_discount(self, percentage):
        discount_amount=self.price *(percentage /100)
        new_price = self.price - discount_amount
        return new_price

    def is_affordable(self, budget):
        return self.price <+ budget

    def __str__(self):
        return self.name


class Customer(models.Model):
    c_name = models.CharField(max_length=100)
    product = models.ManyToManyField(Product)

    def total_spent(self):
        total = sum(product.price for product in self.product.all())
        return total
    
    def add_product(self, product):
        self.product.add(product)

    def remove_product(self, product):
        self.product.remove(product)

    def __str__(self):
        return self.c_name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
   

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mode_date = models.DateField(auto_now=True)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='entries')
    
    class Meta:
        Indexes = [
            models.Index(fields=['headline', '-pub_date'])
        ]
    def __str__(self):
        return self.headline

    def add_tag(self, tag_name):
        """Add a tag to the entry"""
        tag, created = Tag.objects.get_or_create(name=tag_name)
        self.tags.add(tag)

    def remove_tag(self, tag_name):
        """Remove a tag from the entry"""
        tag = Tag.objects.filter(name=tag_name).first()
        if tag:
            self.tags.remove(tag)

    def get_tags(self):
        """Get all tags associated with the entry"""
        return self.tags.all()

    def clear_tags(self):
        """Remove all tags from the entry"""
        self.tags.clear()

