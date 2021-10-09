from re import L
from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Groupmsg,NickNames
from  django.contrib.auth.models import  User


class Groupmsgserialized(ModelSerializer):
# serializer/ change the model into json file here
    class Meta:
        model = Groupmsg
        fields = '__all__'

class NicknameSerialized(ModelSerializer):
    # we are using this to serialize object
    class Meta:
        model = NickNames
        fields = '__all__'

class Loginserialized(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'