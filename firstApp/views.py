from django.shortcuts import render, get_object_or_404
from .models import CourseVariety , College
from .forms import CourseVarietyForm
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

def course_college_view(request):
    colleges = None
    if request.method == 'POST':
        form = CourseVarietyForm(request.POST)
        if form.is_valid():
         course_variety = form.cleaned_data['course_variety']
         colleges = College.objects.filter(course_varities=course_variety) 
    
    else:
        form = CourseVarietyForm()
    
    return render(request , 'firstApp/courseColleges.html',{'form': form ,'colleges':colleges , })





