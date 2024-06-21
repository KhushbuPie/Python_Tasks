from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    mobile = models.CharField(max_length=12)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    address = models.CharField(max_length=255)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6)
    hobbies = models.TextField()

    def __str__(self):
        return self.fname


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    fname = models.CharField(max_length=100)
    lanme = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    Department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.fname
    

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student','Student'),
        ('principal','Principal'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
    
    def __str__(self):
        return self.username
    