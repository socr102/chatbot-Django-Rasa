from django.db import models 


class FlowChatTracker(models.Model):
    chatid = models.CharField(max_length = 5000,default="", blank=True)
    bestway = models.CharField(max_length=100,default="", blank=True)
    emailAddress = models.EmailField(max_length = 50, blank=True)
    zipCode = models.IntegerField(default = 0,blank=True)
    
