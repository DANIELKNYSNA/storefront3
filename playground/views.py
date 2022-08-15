from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging
import requests

logger = logging.getLogger(__name__)  # this translates to playground.views


class HelloView(APIView):
    # @method_decorator(cache_page(5*60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': data})


@cache_page(5 * 60)
def say_hello(request):
    pass
    # this gives us a delay of 2 seconds at this endpoint, simulating a slow api call
