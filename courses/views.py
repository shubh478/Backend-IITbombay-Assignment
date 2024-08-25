from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseInstanceListCreateView(APIView):
    def get(self, request, year, semester):
        instances = CourseInstance.objects.filter(year=year, semester=semester)
        serializer = CourseInstanceSerializer(instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseInstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

   
