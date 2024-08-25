# courses/tests/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Course, CourseInstance

class CourseAPITests(APITestCase):

    def setUp(self):
        # Create a sample course for testing
        self.course = Course.objects.create(
            title='Sample Course',
            course_code='SC101',
            description='This is a sample course.'
        )

    def test_course_list_create(self):
        # Test GET request to list courses
        response = self.client.get(reverse('course-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test POST request to create a new course
        data = {
            'title': 'New Course',
            'course_code': 'NC102',
            'description': 'This is a new course.'
        }
        response = self.client.post(reverse('course-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_detail(self):
        # Test GET request for course detail
        response = self.client.get(reverse('course-detail', kwargs={'pk': self.course.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_instance_list_create(self):
        # Create a course instance for testing
        instance = CourseInstance.objects.create(
            course=self.course,
            year=2024,
            semester=1
        )

        # Test GET request to list course instances
        response = self.client.get(reverse('instance-list', kwargs={'year': 2024, 'semester': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test POST request to create a new course instance
        data = {
            'course': self.course.pk,
            'year': 2024,
            'semester': 1
        }
        response = self.client.post(reverse('instance-list', kwargs={'year': 2024, 'semester': 1}), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_instance_detail(self):
        # Test GET request for instance detail
        response = self.client.get(reverse('instance-detail', kwargs={'year': 2024, 'semester': 1, 'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)