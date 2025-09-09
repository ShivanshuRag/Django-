
from django.urls import path
from . import views

urlpatterns = [
   
    path('' , views.first_App , name='first_App')
]