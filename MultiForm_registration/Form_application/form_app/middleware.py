from django.shortcuts import redirect
# import logging
# logger = logging.getLogger(__name__)

class RoleRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path_info == '/login/': 
            if request.user.is_authenticated:
                print(f"User authenticated in middleware: {request.user.username}, Role: {request.user.role}")
                if request.user.role == 'student':
                    return redirect('student_form')
                elif request.user.role == 'teacher':
                    return redirect('teacher_form')
                # else:
                #     return redirect('index')  
        return response
