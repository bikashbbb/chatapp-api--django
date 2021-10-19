from django.contrib.auth.models import User
from django.db import models
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Groupmsg,Groupmsgserialized, Loginserialized

# messeges related views here
@api_view(['GET'])
def get_groupmsg(request):
    # TODO: GET THE DATA BASE SHOWN IN HERE , THIS IS GET PAGE
    _response = Groupmsg.objects.all()
    # get the objects to be serialized 
    # serialize the model objects
    serialized_objects = Groupmsgserialized(_response,many=True)
    return Response(serialized_objects.data)  
    # this data instance returns list of json data as it gets processd in serializer

@api_view(['POST'])
def post_messeges(request):
    # when clicked on the post button the json data will be requested as data 
    body = request.data
    # data instance gives me the json response coming from request/ post click garesi
    Groupmsg.objects.create(userid= body['userid'],
    messege = body['messege'],
    messege_sent_at = body['messege_sent_at'],
    images = body['images']
    )    
    return Response({
        "object": "created sucessfully"
    })



