from django.http import HttpResponseForbidden
from django.utils.html import format_html

class Custom403Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 403:
            return self.handle_403(request)
        return response

    def handle_403(self, request):
        # Customize the 403 Forbidden response here
        message = "Bid should be more than previous bids"
        
        # Create an HTML response with the image and message
        html_content = format_html("<h1>{}</h1><img src='https://http.cat/images/403.jpg' alt='Forbidden'>", message)
        response = HttpResponseForbidden(content=html_content, content_type='text/html')
        
        return response
