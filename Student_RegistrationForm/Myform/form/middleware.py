import time

class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time


        response['Custom-Header'] = 'Hello, Middleware!'
        response['X-Request-Duration'] = str(duration)
        
        return response
