from rest_framework import viewsets
from .models import student, staff, course, unit
from .serializers import StudentSerializer, StaffSerializer, CourseSerializer, UnitSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = staff.objects.all()
    serializer_class = StaffSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = course.objects.all()
    serializer_class = CourseSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = unit.objects.all()
    serializer_class = UnitSerializer
