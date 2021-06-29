import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time,os,uuid,json,re,sched, timeit,django  
from .analyzer import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT.settings')
django.setup()

from root.models import ChatTracker
from root.models import FlowChatTracker


chat_start = False


def generateReply(chatid,incoming_message): 

    ischatidexist = ChatTracker.objects.filter(chatid=chatid).exists()
    if ischatidexist:pass
    else:ChatTracker(chatid=chatid).save()

    currentchat = ChatTracker.objects.get(chatid=chatid)
    avaliable_choices = ['email','mail','phone']


    if currentchat.bestway=='':                          
        bestway = selectedChoice(incoming_message)
        if bestway in avaliable_choices:
            currentchat.bestway = bestway
            currentchat.save()
            if currentchat.bestway=='mail' or currentchat.bestway=='email':
                reply = "Please enter 4 digit pin code"
                print(reply)
                return reply
            elif currentchat.bestway=='phone':
                reply = "Please enter your PHONE NUMBER"
                print(reply)
                return reply
        else:
            reply = "Please provide a valid choice through which we can reach you out."
            print(reply)
            return reply

    elif currentchat.bestway !='':
        if currentchat.bestway=='mail' or currentchat.bestway=='email':
            # extract 4 digit pin code
            pincode = extractpincode(incoming_message)
            if pincode!=[]:
                currentchat.fourdigitpin=pincode
                currentchat.save()
                reply = "Thanks for providing details. Posting data to SERVER"
                print(reply)
                return reply
            else:
                reply = "Please provide a valid PIN CODE"
                print(reply)
                return reply

        elif currentchat.bestway=='phone':
            # extract phone number 
            if currentchat.phonenumber=='':
                phone = extractphone(incoming_message)
                if phone!='':
                    currentchat.phonenumber = phone
                    currentchat.save()
                    reply = "Please Enter PIN CODE"
                    print(reply) 
                    return reply
                else:
                    reply = "Please enter a valid PHONE NUMBER"
                    print(reply)
                    return reply
            else:
                pincode = extractpincode(incoming_message)
                if pincode!=[]:
                    print(pincode)
                    currentchat.fourdigitpin=pincode
                    currentchat.save()
                    reply  = "Thanks for providing details. Posting data to SERVER"
                    print(reply)
                    return reply
                else:
                    reply = "Please provide a valid PIN CODE"
                    print(reply)
                    return reply

def generateReplyflowchart(chatid,incoming_message):
    global chat_start
    
    if chat_start==False:
        reply = "Hello! I am a bot  here to help"
        chat_start=True
        return reply
    
    ischatidexist = FlowChatTracker.objects.filter(chatid=chatid).exists()
    if ischatidexist:
        pass
    else:
        FlowChatTracker(chatid=chatid).save()
    
    flowChat = FlowChatTracker.objects.get(chatid=chatid)
    avaliable_choices = ['zip','email']
    
    if flowChat.bestway=='':
        bestway = selectedChoice(incoming_message)
        if bestway in avaliable_choices:
            flowChat.bestway = bestway
            flowChat.save()
            
            if flowChat.bestway=='zip':
                reply = "What is your zip code?"
                return reply
        else:
            reply = "Please provide a valid choice through which we can reach you out."             
            return reply
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
                reply = "That zip code was not valid"
                return reply    
         elif flowChat.bestway == 'email':
            #check the real email address 
            isEmail = checkEmailAddress(incoming_message)
            
            if isEmail=='yes':
                reply = "YAY, Thank You! 🎉\nThis will just take a few seconds 😊You are on your way to a FREE phone! "
                flowChat.emailAddress = incoming_message
                flowChat.save() 
                return reply    
            else:
                reply = "What is your email address? (Ex: example@mail.com) 💬"
                return reply 

    

        