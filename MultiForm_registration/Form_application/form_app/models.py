from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.username}-{self.role}'

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
    t_fname = models.CharField(max_length=100)
    t_lname = models.CharField(max_length=100)
    t_email = models.EmailField(unique=True)
    t_subject = models.CharField(max_length=100)
    t_department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.t_fname
    
    
