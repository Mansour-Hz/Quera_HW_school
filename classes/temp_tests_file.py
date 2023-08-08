from django.test import TestCase
from classes.serializers import ClassroomSerializer
from classes.models import Classroom


class ClassroomSerializerTest(TestCase):

    def setUp(self):
        self.classroom_attributes = {
            'capacity': 6,
            'area': 34
        }

        self.classroom = Classroom.objects.create(**self.classroom_attributes)
        self.serializer = ClassroomSerializer(instance=self.classroom)

    def test_contains_expected_fields(self):
        data = self.serializer.data

    def test_capacity_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['capacity'], self.classroom_attributes['capacity'])

    def test_capacity_upper_bound(self):

        self.serializer_data['capacity'] = 5

        serializer = ClassroomSerializer(data=self.serializer_data)

        self.assertTrue(serializer.is_valid())

    def test_capacity_lower_bound(self):

        self.serializer_data['capacity'] = 4

        serializer = ClassroomSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())

    def test_area_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['area'], self.classroom_attributes['area'])

    def test_area_upper_bound(self):
        self.serializer_data['area'] = 5

        serializer = ClassroomSerializer(data=self.serializer_data)

        self.assertTrue(serializer.is_valid())

    def test_area_lower_bound(self):
        self.serializer_data['area'] = -5

        serializer = ClassroomSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())
