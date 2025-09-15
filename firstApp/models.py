from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    

#  One to many relations

class CourseReview(models.Model):
    course = models.ForeignKey(CourseVariety , on_delete=models.CASCADE , related_name="review")
    user = models.ForeignKey(User, on_delete=models.CASCADE  )
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.course.name}'
    
# many to many 

class College(models.Model):
    college_name = models.CharField(max_length=100)
    collage_location = models.CharField(max_length=100)
    course_varities = models.ManyToManyField(CourseVariety , related_name="college")

    def __str__(self):
        return self.college_name
    

# one to one 

class CourseCertificate(models.Model):
    course = models.OneToOneField(CourseVariety , on_delete=models.CASCADE ,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()


    def __str__(self):
        return f'Certificate for {self.course.name}'


