from django.contrib import admin
from .models import CourseVariety ,College ,CourseCertificate,CourseReview

# Register your models here.

class CourseReviewInline(admin.TabularInline):
  model = CourseReview
  extra = 1

class CourseVarityAdmin(admin.ModelAdmin):
  list_display = ('name' , 'type' , 'date_added')
  inlines = [CourseReviewInline]

class CollegeAdmin(admin.ModelAdmin):
  list_display = ('college_name' , 'collage_location')
  filter_horizontal =('course_varities',)

class CourseCertificateAdmin(admin.ModelAdmin):
  list_display = ('course' , 'certificate_number' , 'issued_date' , 'valid_until')


admin.site.register(CourseVariety , CourseVarityAdmin)
admin.site.register(College , CollegeAdmin)
admin.site.register(CourseCertificate , CourseCertificateAdmin)

