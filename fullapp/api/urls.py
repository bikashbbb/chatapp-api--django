from django.urls.conf import  path
from .views import get_groupmsg,post_messeges
from .nickname_views import get_all_nickname,post_nickname,del_nickname,get_individual_nickname,update_nickname
from .loginviews import user_authentication,create_user


# TODO: MAKE AUTHETICATION TO ACESS THE GROUPCHAT PAGE OF API WITH TOKEN
urlpatterns = [
    # GROUP MESSEGE
    path('groupmesseges/',get_groupmsg),
    path('groupmesseges/postmsg/',post_messeges),
    #    nickname
    path('groupmesseges/nickname/',get_all_nickname),
    path('groupmesseges/nickname<str:uid>/create',post_nickname),
    path('nickname/<str:uid>/delete/',del_nickname),
    path('individual/<str:uid>/getnick/',get_individual_nickname),
    path('update/nickname',update_nickname),
    # ########### LOGIN
    path('groupmesseges/<str:usr>/users/',user_authentication),
    path('create/newuser/',create_user),
    
]