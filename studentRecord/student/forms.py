from django import forms
from .models import StudentInfo
 
 
# creating a form
class StudentForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = StudentInfo
 
        # specify fields to be used
        fields = [
            "Rollno",
            "Name",
            "Class",
            "School",
            "Mobile",
            "Address"
        ]

