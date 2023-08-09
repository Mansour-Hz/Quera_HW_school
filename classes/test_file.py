from django.test import TestCase
from .serializers import ClassroomSerializer
from .models import Classroom


class ClassroomSerializerTest(TestCase):

    def setUp(self):
        self.classroom_attributes = {
            'capacity': 6,
            'area': 34.00,
            'name': 'A-1',
        }

        self.classroom = Classroom.objects.create(**self.classroom_attributes)
        self.serializer = ClassroomSerializer(instance=self.classroom)


    def test_contains_expected_fields(self):
        data = self.serializer.data


    def test_capacity_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['capacity'], self.classroom_attributes['capacity'])


    def test_capacity_upper_bound(self):

        self.classroom_attributes['capacity'] = 5

        serializer = ClassroomSerializer(data=self.classroom_attributes)

        self.assertTrue(serializer.is_valid())


    def test_capacity_lower_bound(self):

        self.classroom_attributes['capacity'] = 4

        serializer = ClassroomSerializer(data=self.classroom_attributes)

        self.assertFalse(serializer.is_valid())


    def test_area_field_content(self):
        data = self.serializer.data

        print(data['area'], type(data['area']))
        print(self.classroom_attributes['area'], type(self.classroom_attributes['area']))

        self.assertEqual(data['area'], self.classroom_attributes['area'])


    def test_area_upper_bound(self):
        self.classroom_attributes['area'] = 5

        serializer = ClassroomSerializer(data=self.classroom_attributes)

        self.assertTrue(serializer.is_valid())


    def test_area_lower_bound(self):
        self.classroom_attributes['area'] = -5

        serializer = ClassroomSerializer(data=self.classroom_attributes)

        self.assertFalse(serializer.is_valid())
