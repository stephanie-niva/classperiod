from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import ClassroomListView
from .views import ClassPeriodListView
from .views import CourseListView
from .views import StudentDetailView
from .views import CourseDetailView
from .views import ClassPeriodDetailView
from .views import ClassroomDetailView
urlpatterns=[
    path("student/",StudentListView.as_view(),name="student_list_view"),
    path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
    path("classroom/",ClassroomListView.as_view(),name="classroom_list_view"),
     path("course/",CourseListView.as_view(),name="course_list_view"),
    path("classperiod/",ClassPeriodListView.as_view(),name="classperiod_list_view"),
    path("student/<int:id>", StudentDetailView.as_view(), name="student_Detail_views"),
    path("course/<int:id>", CourseDetailView.as_view(), name="Course_Detail_view"),
    path("class/<int:id>", ClassPeriodDetailView.as_view(), name="classPeriod_Details_views"),
    path("classroom/<int:id>", ClassroomDetailView.as_view(), name="classroom_details_views")
]