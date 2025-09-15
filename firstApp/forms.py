from django import forms
from .models import CourseVariety

class CourseVarietyForm(forms.Form):
    course_variety = forms.ModelChoiceField(queryset=CourseVariety.objects.all() , label='Select Course Variety')