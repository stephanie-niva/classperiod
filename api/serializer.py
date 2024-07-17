from  rest_framework import serializers
from student.models import Student
from  classes.models import Classroom
from course.models import course
from teacher.models import Teacher
class StudentSerializer(serializers.ModelSerializer):
      class Meta:
           model= Student
           fields="__all__"
class ClassesSerializer(serializers.ModelSerializer):
      class Meta:
           model= Classroom
           fields="__all__"
class CourseSerializer(serializers.ModelSerializer):
      class Meta:
           model= course
           fields="__all__"
class TeacherSerializer(serializers.ModelSerializer):
      class Meta:
           model= Teacher
           fields="__all__"
