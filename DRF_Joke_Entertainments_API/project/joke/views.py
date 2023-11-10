import requests
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from . import views

from .models import Joke, Entertainments
from .serializers import JokeSerializer
from .serializers_2 import EntertainmentsSerializer


class JokeEntertainmentsViewSet(APIView):
    permission_classes = [AllowAny]
    serializer_class = None
    api_url = None


class JokeViewSet(JokeEntertainmentsViewSet):
    serializer_class = JokeSerializer
    api_url = 'https://official-joke-api.appspot.com/random_joke'

    def post(self, request):

        response = requests.get(self.api_url)
        self.serializer_class.save_response(response.json(), response_data=response.json())
        return Response(response.json(), status=response.status_code)


class EntertainmentsViewSet(JokeEntertainmentsViewSet):
    serializer_class = EntertainmentsSerializer
    api_url = 'http://www.boredapi.com/api/activity'

    def post(self, request):
        response = requests.get(self.api_url)
        self.serializer_class.save_response(response.json(), response_data=response.json())
        return Response(response.json(), status=response.status_code)
