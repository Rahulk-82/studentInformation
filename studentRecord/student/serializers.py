from rest_framework import serializers 
from student.models import StudentInfo
from student.models import StudentAcademics
 
class StudentInfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = StudentInfo
        fields = '__all__'

                  
class StudentAcademicsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = StudentAcademics
        fields = '__all__'
