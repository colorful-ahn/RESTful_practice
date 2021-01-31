from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import Prac_User
from .serializer import Prac_UserSerializer


class SignUp(APIView):
    def post(self, request, format=None):
        try:
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            user = Prac_User.objects.create_user(username=username, password=password ,email=email)
            return JsonResponse({"True"})
        except Exception as e:
            return JsonResponse({"False"})