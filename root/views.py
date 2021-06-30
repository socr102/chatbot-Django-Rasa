from django.http.response import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .script import   generateReplyflowchart 

  
def index(request,chatid,incoming_message): 
    reply = generateReplyflowchart(chatid,incoming_message)
    return JsonResponse({"message":reply})



