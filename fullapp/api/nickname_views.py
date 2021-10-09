import re
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import NicknameSerialized,NickNames
from rest_framework.response import Response

@api_view(['GET'])
def get_all_nickname(request):
    current_object = NickNames.objects.all()
    serialized_obj = NicknameSerialized(current_object,many=True)
    return Response(serialized_obj.data)

@api_view(['DELETE'])
def del_nickname(request,uid):
    # TODO:DELETE THE NICKNAME
    NickNames.objects.get(userid = uid).delete()
    return Response({'info': 'nickname object deleted sucessfully'})
    

@api_view(['POST'])
def post_nickname(request,uid):
    # TODO: create nickname object
    new_nickname = NickNames.objects.create(userid= uid,nickname= request.data['nickname'])
    Serializer_obj = NicknameSerialized(new_nickname)
    return Response(Serializer_obj.data)

@api_view(['PUT'])
def update_nickname(request):
    # put button click garesi put request hanxa ani tyo input chai request ma aauxa as data
    # update the nickname
    user = NickNames.objects.get(userid= request.data['userid'])
    user.nickname = request.data['new_nickname']
    user.save()
    return Response({
        "nickname":user.nickname
    })

@api_view(['GET'])
def get_individual_nickname(request,uid):
    # TODO: GET NICKNAME WITH INDIVIDUAL UID
    new_obj = NickNames.objects.get(userid=uid)
    serialized_obj = NicknameSerialized(new_obj)
    return Response(serialized_obj.data)