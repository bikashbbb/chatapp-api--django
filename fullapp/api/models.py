from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Groupmsg(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE) # has realtion with the User  mnodel
    messege = models.TextField(null= True)
    messege_sent_at = models.TimeField(auto_now=False, auto_now_add=False)
    images = models.ImageField(null= True,blank = True,upload_to= "images/")
    # image nahuna ni payo ki messege nahuna ni payoo..

    def __str__(self) -> str:
        return str(self.messege_sent_at)
    
    class Meta:
        ordering = ['messege_sent_at']

class NickNames(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)






