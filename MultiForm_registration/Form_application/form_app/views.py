from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth import get_user_model
from .models import CustomUser, Student , Teacher
# from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm , TeacherForm
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required



# def user_signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password1']
#             role = form.cleaned_data['role']
            
#             user = CustomUser(username=username, email=email, password=password)
#             user.set_password(password)
#             user.save()
#             return redirect('user_login')
#             # if role == 'student':
#             #     return redirect('student_form')
#             # elif role == 'teacher':
#             #     return redirect('teacher_form')
#             # else:
#             #     return redirect('login')

#     else:
#         form = SignupForm()
#     return render(request, 'form_app/signup.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            role = form.cleaned_data['role']
            
            user = CustomUser(username=username, email=email, role=role)  # Set role here
            user.set_password(password)
            user.save()
            return redirect('user_login')

    else:
        form = SignupForm()
    return render(request, 'form_app/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"User authenticated: {request.user.username}, Role: {request.user.role}")
                if user.role == 'student':
                    return redirect('student_form')
                elif user.role == 'teacher':
                    return redirect('teacher_form')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'form_app/login.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return JsonResponse({'status': 'success'})  # Return success response
#             else:
#                 return JsonResponse({'status': 'error', 'message': 'Invalid username or password'})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'Form is not valid'})
#     else:
#         form = LoginForm()
#     return render(request, 'form_app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
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
        form = StudentForm()
    return render(request, 'form_app/student_form.html', {'form': form})

@login_required
def teacher_form(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            try:
                # Create a new Student object and save it to the database
                t_fname = form.cleaned_data['t_fname']
                t_lname = form.cleaned_data['t_lname']
                t_email = form.cleaned_data['t_email']
                t_subject = form.cleaned_data['t_subject']
                t_department = form.cleaned_data['t_department']
                
                teacher = Teacher(t_fname=t_fname, t_lname=t_lname, t_email=t_email, t_subject=t_subject, t_department=t_department)
            
                teacher.save()
                # student.save()
                # student.hobbies.set(hobbies)  
                return JsonResponse({'success': True})
                # return redirect('registration_success')  
            except IntegrityError:
                form.add_error('email', 'Email is already registered.')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = TeacherForm()
    return render(request, 'form_app/teacher_form.html', {'form': form})




