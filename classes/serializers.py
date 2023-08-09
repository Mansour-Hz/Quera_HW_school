from rest_framework import serializers
from .models import Classroom

# Classroom Serializer
class ClassroomSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(required=False, min_value=5)
    area = serializers.DecimalField(required=False, max_digits=5, decimal_places=2, min_value=5.00)

    class Meta:
        model = Classroom
        fields = '__all__'
