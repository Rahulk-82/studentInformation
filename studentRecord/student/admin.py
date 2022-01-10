from django.contrib import admin

# Register your models here.
from .models import StudentInfo
from .models import StudentAcademics

admin.site.register(StudentInfo)
admin.site.register(StudentAcademics)

