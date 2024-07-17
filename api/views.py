from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework.views import APIView
from  student.models import Student
from  classes.models import Classroom
from teacher.models import Teacher
from course.models import course
from.serializer import StudentSerializer
from.serializer import TeacherSerializer
from.serializer import  CourseSerializer
from.serializer import   ClassesSerializer

class StudentListView(APIView):
    def get(self,request):
        student=Student.objects.all
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
class ClassesListView(APIView):
    def get(self,request):
        classes = Classroom.objects.all
        serializer=ClassesSerializer(classes,many=True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all
        serializer= TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self,request):
        course= course.objects.all
        serializer=CourseSerializer(course,many=True)
        return Response(serializer.data)


# Create your views here.
