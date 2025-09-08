from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("this about me , I a shivanshu ") 

    return render( request , 'index.html')


def about(request):
    return HttpResponse("this about me , I a shivanshu ")

def contact(request):
    return HttpResponse("This is my contact : shivanshu@gmail.com ")