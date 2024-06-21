from django.urls import path
from form.views import register_student,StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView , MultipleFormsView, test_view
from django.views.generic import TemplateView
from django.contrib import admin
from form import views


urlpatterns = [
    path('students/', register_student, name='register_student'),
    # path('registration-success/', registration_success, name='registration_success'),
    path('registration_success/', TemplateView.as_view(template_name="form/registration_success.html"), name='registration_success'),
    path('', StudentListView.as_view(), name='student_list'),
    path('student_detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student_form'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student_confirm_delete'),

    # path('multiple_forms/', MultipleFormsView.as_view(), name='multiple_forms'),

    # path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('teacher/', views.teacher_home, name='teacher_home'),
    path('student/', views.student_home, name='student_home'),
    path('register/student/', views.register_student, name='register_student'),    
    path('test/', test_view, name='test_view'),
]
