from django.db import models
from django.contrib.auth.models import User


class Topic (models.Model):
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE) #har kasi tapike 
                                            # kelid khareji esme user hast(request.user)    #khodesho mibine.       

    def __str__(self):
        return self.text
    
class  Entry(models.Model):
    topic= models.ForeignKey(Topic, on_delete=models.CASCADE)# topic_id
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'

        def __str__(self):
            return f"{self.text[ : 50]}. . . "
        
