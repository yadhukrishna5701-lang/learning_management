from django.urls import path

from course_management.views import SignUpView
from course_management.views import CourseListCreateView
from course_management.views import CourseRetrieveUpdateDeleteView


urlpatterns = [
    path("register/",SignUpView.as_view()),
    path("list/",CourseListCreateView.as_view()),
    path("create/",CourseListCreateView.as_view()),
    path("<int:pk>/",CourseRetrieveUpdateDeleteView.as_view()),
   
]