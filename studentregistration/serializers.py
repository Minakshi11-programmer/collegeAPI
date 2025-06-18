from rest_framework import serializers
from .models import student, staff, course, unit

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = staff
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = unit
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)
    
    class Meta:
        model = course
        fields = '__all__'
