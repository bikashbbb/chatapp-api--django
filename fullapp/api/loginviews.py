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
        # if authentication method doesnt return null 
        # return the field data of the current user.
        # if authentication method doesnt return null
        auth.login(request,curent_user)
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
        new_user = User.objects.create(username = request.data['username'])
        new_user.set_password(request.data['password'])
        new_user.save()
        serialize = Loginserialized(new_user) 
        return Response(serialize.data)
    # data has the json input
    except Exception :
        return Response({"username":"username already taken ###@"})
        
   # TODO : GET IF USER IS LOGGED IN OR NOT
