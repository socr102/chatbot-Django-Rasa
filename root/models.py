from django.db import models 

class ChatTracker(models.Model): 
    chatid = models.CharField(max_length=5000,default="", blank=True,)
 
    bestway = models.CharField(max_length=100,default="", blank=True)
     
    phonenumber = models.CharField(max_length=100,default="", blank=True)
     
    fourdigitpin = models.IntegerField(default=0, blank=True)

class FlowChatTracker(models.Model):
    chatid = models.CharField(max_length = 5000,default="", blank=True)
    bestway = models.CharField(max_length=100,default="", blank=True)
    emailAddress = models.EmailField(max_length = 50, blank=True)
    zipCode = models.IntegerField(default = 0,blank=True)
    
