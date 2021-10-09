import re
from .serializers import User, Loginserialized
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import auth

@api_view(['GET'])
def user_authentication(request,usr):
    # get users with the help of username..
    username = usr.split('_')
    curent_user = auth.authenticate(username=username[0],password= username[1])
    if curent_user != None:
        Loginserialized_obj = Loginserialized(curent_user)
        return Response(Loginserialized_obj.data)
    else:
        return Response({
            "username":"null"
        })

@api_view(['POST'])
def create_user(request):
    # TODO: CREATE A USER
    try:
        User.objects.create(username = request.data['username'],password = request.data['password'])
        return Response({"output":"user created sucessfully"})
    # data has the json input
    except Exception :
        return Response({"output":"username already taken"})
