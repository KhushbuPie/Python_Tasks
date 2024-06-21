from django import forms
from django.core.validators import RegexValidator
from .models import Department, Student, Teacher, CustomUser
from django.contrib.auth.forms import UserCreationForm


class StudentRegistrationForm(forms.Form):
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
    class Meta:
        model = Student
        fields = [
            "fname", "lname", "email", "dob", "mobile", "gender",
            "address", "department", "pincode", "hobbies"
        ]
        widgets = {
            'fname': forms.TextInput(attrs={'placeholder': 'Enter Your First Name', 'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'placeholder': 'Enter Your Last Name', 'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter date of birth', 'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')]),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email Id', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter Your mobile number', 'class': 'form-control'}),
            'department': forms.Select(attrs={'placeholder': 'Select Department', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter Your Address', 'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'placeholder': 'Enter Your Pin Code', 'class': 'form-control'})
        }
    
# class TeacherForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = ['fname', 'lname', 'email', 'subject', 'department']

class TeacherForm(forms.Form):
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
    email = forms.EmailField(
        label="Email Id",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Id', 'class':'form-control'})
    )
    subject = forms.CharField(
        label="Subject ",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Subject', 'class':'form-control'})
    )
    department = forms.ModelChoiceField(
        label="Department",
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'placeholder':'Select Departmnet','class':'form-control'})
    )

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('role',)