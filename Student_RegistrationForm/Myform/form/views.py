from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import StudentRegistrationForm , TeacherForm
from .models import Student, Teacher
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView ,DetailView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .mixins import FormMixin
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from form.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            try:
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                email = form.cleaned_data['email']
                dob = form.cleaned_data['dob']
                gender = form.cleaned_data['gender']
                mobile = form.cleaned_data['mobile']  
                department = form.cleaned_data['department']
                address = form.cleaned_data['address']
                pincode = form.cleaned_data['pincode']
                hobbies = form.cleaned_data['hobbies']
                
                student = Student(
                    fname=fname, lname=lname, email=email, dob=dob, mobile=mobile,
                    gender=gender, department=department, address=address, pincode=pincode,
                    hobbies=hobbies  
                )
                student.save()
                # student.hobbies.set(hobbies)  
                return JsonResponse({'success': True})
                # return redirect('registration_success')  
            except IntegrityError:
                form.add_error('email', 'Email is already registered.')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = StudentRegistrationForm()
    return render(request, 'form/register_student.html', {'form': form})


class StudentListView(ListView):
    model = Student
    template_name = 'form/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'form/student_detail.html'
    context_object_name = 'student_detail'

class StudentUpdateView(UpdateView):
    model=Student   
    fields = [
        "id","fname", "lname", "email","dob","mobile","gender",
        "address","department","pincode","hobbies"
    ]
    success_url = reverse_lazy('student_list')

    def get_object(self, queryset=None):
        return Student.objects.get(pk=self.kwargs['pk'])


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'form/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

class MultipleFormsView(View):
    def get(self, request, *args, **kwargs):
        student_form = StudentRegistrationForm()
        teacher_form = TeacherForm()
        return render(request, 'form/multiple_forms.html', {'student_form': student_form, 'teacher_form': teacher_form})

    def post(self, request, *args, **kwargs):
        student_form = StudentRegistrationForm(request.POST)
        teacher_form = TeacherForm(request.POST)

        if student_form.is_valid() and teacher_form.is_valid():
            # student_form.save()
            # teacher_form.save()
            fname = student_form.cleaned_data['fname']
            lname = student_form.cleaned_data['lname']
            email = student_form.cleaned_data['email']
            dob = student_form.cleaned_data['dob']
            gender = student_form.cleaned_data['gender']
            mobile = student_form.cleaned_data['mobile']  
            department = student_form.cleaned_data['department']
            address = student_form.cleaned_data['address']
            pincode = student_form.cleaned_data['pincode']
            hobbies = student_form.cleaned_data['hobbies']

            #teacher form

            t_fname = teacher_form.cleaned_data['fname']
            t_lname = teacher_form.cleaned_data['lname']
            t_email = teacher_form.cleaned_data['email']
            t_subject = teacher_form.cleaned_data['subject']
            t_department = teacher_form.cleaned_data['department']

            student = Student(
                    fname=fname, lname=lname, email=email, dob=dob, mobile=mobile,
                    gender=gender, department=department, address=address, pincode=pincode,
                    hobbies=hobbies  
                )
                
            student.save()
            teacher = Teacher(fname=t_fname, lanme=t_lname, email=t_email, subject=t_subject, Department=t_department)
            
            teacher.save()


            return redirect('student_list')  

        return render(request, 'form/multiple_forms.html', {'student_form': student_form, 'teacher_form': teacher_form})


# Custome Middleware

User = get_user_model()
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'form/login.html')

def home_view(request):
    return render(request, 'form/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'form/login.html')

def signup_view(request):
    if request.method == 'POST':
        print(request.POST['username'])
        print(request.POST['password1'])
        print(request.POST['role'])
        form = CustomUserCreationForm(request.POST)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            print("Valid")
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        print("HI")

    return render(request, 'form/signup.html',{'form':form})

@login_required
def teacher_home(request):
    print("Welcome Teacher")
    return render(request, 'form/teacher.html')

@login_required
def student_home(request):
    print("Welcome Student")
    return render(request, 'form/student.html')


def test_view(request):
    return HttpResponse("This is a test view.")
