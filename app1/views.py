import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.



def home(request):
    return render (request,'home.html');

def aboutus(request):
    return render(request,'aboutus.html');

def email(request):
    return render (request,'email.html');
def contactus(request):
    return render (request,'contactus.html');
def project1(request):
    if request.method == 'POST':
        var1=request.POST['yname']
        var2=request.POST['email']
        var3=request.POST['service']
        var4=request.POST['budget']
        var5=request.POST['message']
        var6="Welcome dear"
        var = var5+var1

        send_mail('Contact form',
             "Name :"+var1+"\n"+"Email :"+var2+"\n"+"Services :"+var3+"\n"+"Budget :"+var4+"\n"+"Message :"+var5 ,
             settings.EMAIL_HOST_USER ,
             ['kamrankhanofficial12@gmail.com'],
           fail_silently=False)     
    return render (request,'project1.html');
def project2(request):
    return render(request,'project2.html');
def project3(request):
    return render(request,'project3.html');