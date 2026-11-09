from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListAPIView,CreateAPIView

from course_management.serializers import UserSerializer,CourseSerializer
from course_management.models import Course

# Create your views here.

class SignUpView(APIView):


    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data = form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_superuser(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data = serializer_instance.data)
        
        else:

            return Response(data = serializer_instance.errors)

from course_management.pagination import CustomPagination
from course_management.pagination import Customlimitoffsetpagination

class CourseListCreateView(ListAPIView,CreateAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser] 
    pagination_class = Customlimitoffsetpagination
    

    serializer_class = CourseSerializer
    queryset = Course.objects.all()


    def get_queryset(self):

        qs = Course.objects.all()

        query_parameter = self.request.query_params


        if "language" in query_parameter:

            language = query_parameter.get("language")

            qs = qs.filter(language__iexact =language)

        if "fee" in query_parameter:

            fee = query_parameter.get("fee")

            qs = qs.filter(fee__iexact =fee)

        if "trainer" in query_parameter:

            trainer = query_parameter.get("trainer")

            qs = qs.filter(trainer__iexact =trainer)

        if "name" in query_parameter:

            name = query_parameter.get("name")

            qs = qs.filter(name__icontains=name)
            
        return qs

    # def get(self,request):

    #     instance = Course.objects.all()

    #     serializer_instance = CourseSerializer(instance,many = True)

    #     return Response(data = serializer_instance.data)

    # def post(self,request):

    #     form_data = request.data

    #     serializer_instance = CourseSerializer(data = form_data)

    #     if serializer_instance.is_valid():

    #         serializer_instance.save()

    #         return Response(data = serializer_instance.data)

    #     else:

    #         return Response(data = serializer_instance.errors)

class CourseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser] 

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    