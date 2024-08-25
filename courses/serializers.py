from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'course_code', 'description']

class CourseInstanceSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_code = serializers.CharField(source='course.course_code', read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True)

    class Meta:
        model = CourseInstance
        fields = ['id', 'course', 'course_title', 'course_code', 'year', 'semester']

    def create(self, validated_data):
        
        course = validated_data.pop('course')
        instance = CourseInstance.objects.create(course=course, **validated_data)
        return instance
