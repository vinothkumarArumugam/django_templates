from django.shortcuts import render
import datetime

def display(request):
    date=datetime.datetime.now()
    date_dict={'display_date':date}   # template tags in dict data structure
    return render(request,'templatedemoapp/ab.html',context=date_dict) #context must give key name of the dict

#we dont use httpresponse ,we are rendering this to .html file
