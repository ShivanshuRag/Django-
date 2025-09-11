from django.shortcuts import render, get_object_or_404
from .models import CourseVariety

# Create your views here.

def first_App(request):
    courses = CourseVariety.objects.all()
    return render(request , 'firstApp/firstApp.html' ,{'courses': courses})

def course_Detail(request, course_id):
    detail = get_object_or_404(CourseVariety , pk=course_id)
    return render(request , 'firstApp/courseDetails.html' , {'detail': detail})

def course_Price(request , price_id):
    paisa = get_object_or_404(CourseVariety , pk=price_id)
    return render(request , 'firstApp/coursePrice.html' , {'paisa': paisa} )