from rest_framework import serializers
from .models import Sensor, Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id' ,'name' , 'description', 'measurement']
