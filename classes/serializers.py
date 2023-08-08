from rest_framework import serializers
from models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):

    capacity = serializers.FloatField(min_value=5)
    area = serializers.FloatField(min_value=0)

    class Meta:
        model = Classroom
        fields = ['id', 'name', 'capacity', 'area']
