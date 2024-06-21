from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.index, name='index'),  
    path('', TemplateView.as_view(template_name="form_app/index.html"), name='index'),
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('student_form/', views.student_form, name='student_form'),
    path('teacher_form/', views.teacher_form, name='teacher_form')


]
