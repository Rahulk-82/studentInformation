from django.db import models

# Create your models here.

    
class StudentInfo(models.Model):
    Rollno=models.IntegerField(max_length=2, blank=False, default='',primary_key=True,unique=True)
    Name = models.CharField(max_length=70, blank=False, default='')
    Class=models.IntegerField(max_length=2, blank=False, default='')
    School=models.CharField(max_length=200, blank=False, default='')
    Mobile=models.IntegerField(max_length=10, blank=False, default='')
    Address=models.CharField(max_length=200, blank=False, default='')
    


class  StudentAcademics(models.Model):
    Rollno=models.ForeignKey('StudentInfo',to_field='Rollno',unique=True,on_delete=models.CASCADE, default='')
    Math=models.IntegerField(max_length=3, blank=False, default='')
    Physics=models.IntegerField(max_length=3, blank=False, default='')
    Chemistry=models.IntegerField(max_length=3, blank=False, default='')
    Biology=models.IntegerField(max_length=3, blank=False, default='')
    English=models.IntegerField(max_length=3, blank=False, default='')
