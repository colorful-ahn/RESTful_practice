from rest_framework import serializers
from .models import Prac_User

class Prac_UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username','email']