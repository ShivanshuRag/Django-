
from django.urls import path
from . import views 

urlpatterns = [
   
    path('' , views.first_App , name='first_App'),
    path('<int:course_id>/', views.course_Detail , name='course_Detail'),
    path('<int:price_id>/p', views.course_Price , name='course_Price'),
    path('courses_colleges/', views.course_college_view , name='courses_colleges')
]