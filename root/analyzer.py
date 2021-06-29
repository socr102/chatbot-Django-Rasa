import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def selectedChoice(message):
    message = str(message).lower()
    if "email" in message:
        choice = "email"
        return choice
    elif "mail" in message:
        choice = "mail"
        return choice
    elif "phone" in message:
        choice = "phone"
        return choice
    elif "zip" in message:
        choice = "zip"
        return choice

 

def extractpincode(message):
    numbers = re.findall('[0-9]+', message)
    if numbers != []:
        pincodes = [x for x in numbers if len(x) == 4]
        if pincodes != []:return pincodes[0]
        else:return []
    else:return []
        
 

def extractphone(message):
    numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', message)
    if numbers != []:
        return numbers[0] 
    else:return []
        

def checkEmailAddress(email):  
    print(email) 
    response = requests.get("https://isitarealemail.com/api/email/validate",params = {"email": email})

    status = response.json()['status']
    if status == "valid":
        return 'yes' 
    elif status == "invalid":
        return 'no'
    else:
        return 'yes'   




# number = orignalnumber.replace('-','').replace('(','').replace(')','').replace('+','').strip()
# if len(number)==11:
#     print(orignalnumber)

#for ChartTracker1 
def extractZipCode(message):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+str(message)+'&key=AIzaSyAJGToD7umZ-VdfAl95vSnd1AlxVxt9lUI')
    status = response.json()['status']
    if status=="OK":
        return "yes"
    else:return "no"    