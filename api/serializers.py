from  rest_framework import serializers
from student.models import Student
from classroom.models import Classroom
from course.models import course
from teacher.models import Teacher
class StudentSerializer(serializers.ModelSerializer):
      class Meta:
           model= Student
           fields="__all__"
class ClassroomSerializer(serializers.ModelSerializer):
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

class ClassPeriodSerializer(serializers.ModelSerializer):
      class Meta:
           model= ClassPeriod
           fields="__all__"













