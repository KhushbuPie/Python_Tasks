# form/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'teacher':
                # Redirect to teacher page
                if not request.path.startswith(reverse('teacher_home')):
                    return redirect('teacher_home')
            elif request.user.role == 'student':
                # Redirect to student page
                if not request.path.startswith(reverse('student_home')):
                    return redirect('student_home')

        return None
