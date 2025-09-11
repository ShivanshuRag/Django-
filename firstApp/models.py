from django.db import models
from django.utils import timezone

# Create your models here.
class CourseVariety(models.Model):
    course_type_choice = [
        ('SD', 'Software Development'),
        ('ML', 'Machine Learning'),
        ('DS', 'Data Scientist'),
        ('AI','Artificial Inteligence'),
        ('DP','Deep Learning'),
        ('EH', 'Ethical Hacking'),
    ]
    

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=course_type_choice, default= 'SD')
    description = models.TextField(default='')
    price = models.IntegerField(default=500)

    def __str__(self):
        return self.name
    
    
    

