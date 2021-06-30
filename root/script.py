import requests
#from bs4 import BeautifulSoup
#from selenium import webdriver
import time,os,uuid,json,re,sched, timeit,django  
from .analyzer import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT.settings')
django.setup()


from root.models import FlowChatTracker


chat_start = False



def generateReplyflowchart(chatid,incoming_message):
    
    #global chat_start
    
    #if chat_start==False:
    #    reply = "Hello! I am a bot  here to help\nWhat is your zip code?"
    #    chat_start=True
    #    return reply
    
    ischatidexist = FlowChatTracker.objects.filter(chatid=chatid).exists()
    if ischatidexist:
        pass
    else:
        FlowChatTracker(chatid=chatid).save()
    
    flowChat = FlowChatTracker.objects.get(chatid=chatid)
    avaliable_choices = ['zip','email','config']#flowchat1 ,flowchat2, flowchat3
    
    if flowChat.bestway=='':
        flowChat.bestway = 'zip'
        flowChat.save()
        reply = "Hello! I am a bot  here to help  , What is your zip code?"
        return reply
        #bestway = selectedChoice(incoming_message)
        #if bestway in avaliable_choices:
        #    flowChat.bestway = bestway
        #    flowChat.save()
            
        #    if flowChat.bestway=='zip':
        #        reply = "What is your zip code?"
        #        return reply
        #else:
        #    reply = "Please provide a valid choice through which we can reach you out."             
        #    return reply
    elif flowChat.bestway !='':            
         if flowChat.bestway=='zip':       
            #extract 5 digit zip code  
            zipcode_status = extractZipCode(incoming_message)
                
            if zipcode_status=="yes":
                flowChat.zipCode = incoming_message
                flowChat.bestway = 'email'
                flowChat.save()
                reply = "What is your email address? (Ex: example@mail.com) 💬"
                return reply
            else:
                reply = "That zip code was not valid "
                return reply    
         elif flowChat.bestway == 'email':
            #check the real email address   
            isEmail = checkEmailAddress(incoming_message)
             
            if isEmail=='yes':
                reply = "Making sure that's a real email 💌   YAY, Thank You! 🎉  This will just take a few seconds 😊You are on your way to a FREE phone! Hurray that was a valid zip code! 🎉 "
                flowChat.emailAddress = incoming_message
                flowChat.bestway = 'config'
                flowChat.save() 
                return reply    
            else:
                reply = "Making sure that's a real email 💌   What is your email address? (Ex: example@mail.com) 💬"
                return reply 
         elif flowChat.bestway == "config":
             #User configuration
            return     
    

        