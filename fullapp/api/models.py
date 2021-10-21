from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Groupmsg(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE) # has realtion with the User  mnodel
    messege = models.TextField(null= True)
    messege_sent_at = models.DateTimeField(null=False, auto_now_add=False,auto_now=False)
    images = models.ImageField(null= True,blank = True,upload_to= "images/")
    # image nahuna ni payo ki messege nahuna ni payoo..

    def __str__(self) -> str:
        return str(self.messege_sent_at)
    
    class Meta:
        ordering = ['-messege_sent_at']
        # save data on descending order. i.e jun date agadiko pacadi save hunxa

def get_name(self):
    return self.username

User.add_to_class("__str__", get_name)

class NickNames(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)






