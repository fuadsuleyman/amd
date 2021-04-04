import uuid
import json
from django.http import HttpResponse
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware

from index.views import home_page

class MyCookieProcessingMiddleware(object):

    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response
        self.cookie = uuid.uuid4().hex
        

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        response = self.get_response(request)
        self.process_view(request, home_page)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """
        Called just before Django calls the view.
        """
        self.process_request(request)
        self.process_response(request, HttpResponse())
        return None

    # your desired cookie will be available in every django view
    def process_request(self, request):
        # will only add cookie if request does not have it already
        if not request.COOKIES.get('device'):
            request.COOKIES['device'] = json.dumps(self.cookie)
        # return request 

    # your desired cookie will be available in every HttpResponse parser like browser but not in django view
    def process_response(self, request, response):
        if not request.COOKIES.get('device'):
            response.set_cookie('device', json.dumps(self.cookie))
        return response

# class MyCookieProcessingMiddleware(SessionMiddleware):


#     def process_response(self, request, response):
#         cookie = uuid.uuid4().hex
#         response = super(MyCookieProcessingMiddleware, self).process_response(request, response)
#         #You have access to request.user in this method
#         if not request.COOKIES.get('device'):
#             response.set_cookie('device', json.dumps(cookie))
#         return response