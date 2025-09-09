from django.shortcuts import render

# Create your views here.

def first_App(request):
    return render(request , 'firstApp/firstApp.html')
