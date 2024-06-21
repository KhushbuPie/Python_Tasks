from django import forms
from django.core.validators import RegexValidator
from .models import Department, Student, Teacher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email','password','role']

class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
    )
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class StudentForm(forms.Form):
    fname = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your First Name', 'class':'form-control'})
    )
    lname = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Last Name', 'class':'form-control'})
    )
    dob = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={'type': 'date','placeholder': 'Enter date of birth', 'class':'form-control'})
    )
    gender = forms.ChoiceField(
        label="Gender",
        choices=[('male','Male'), ('female', 'Female'), ('other', 'Other')],
        widget=forms.RadioSelect
    )
    email = forms.EmailField(
        label="Email Id",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Id', 'class':'form-control'})
    )
    mobile = forms.CharField(
        label="Mobile No.",
        max_length=15,
        validators=[RegexValidator(r'^\d{10}$')],
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your mobile number', 'class':'form-control'})
    )
    department = forms.ModelChoiceField(
        label="Department",
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'placeholder':'Select Departmnet','class':'form-control'})
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Address ', 'class':'form-control'})
    )
    pincode = forms.CharField(
        label="Pin Code",
        max_length=10,
        validators=[RegexValidator(r'^\d{6}$')],
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Pin Code', 'class':'form-control'})
    )
    hobbies = forms.MultipleChoiceField(
        label="Hobbies",
        choices=[
            ('reading', 'Reading'),
            ('travelling', 'Travelling'),
            ('sports', 'Sports'),
            ('music', 'Music'),
            ('art', 'Art')
        ],
        widget=forms.CheckboxSelectMultiple()
    )
    

class TeacherForm(forms.Form):
    t_fname = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your First Name', 'class':'form-control'})
    )
    t_lname = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Last Name', 'class':'form-control'})
    )
    t_email = forms.EmailField(
        label="Email Id",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Id', 'class':'form-control'})
    )
    t_subject = forms.CharField(
        label="Subject ",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Subject', 'class':'form-control'})
    )
    t_department = forms.ModelChoiceField(
        label="Department",
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'placeholder':'Select Departmnet','class':'form-control'})
    )