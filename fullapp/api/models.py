from django.db import models

# Create your models here.
class Groupmsg(models.Model):
    userid = models.IntegerField()
    messege = models.TextField(null= True)
    messege_sent_at = models.DateTimeField()
    images = models.ImageField(null= True,blank = True,upload_to= "images/")
    # image nahuna ni payo ki messege nahuna ni payoo..

    def __str__(self) -> str:
        return str(self.messege_sent_at)
    
    class Meta:
        ordering = ['messege_sent_at']

class NickNames(models.Model):
    userid = models.IntegerField()
    nickname = models.CharField(max_length=50)






