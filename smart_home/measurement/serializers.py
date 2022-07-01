from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensorID', 'temperature', 'date']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description', 'measurements']


class oneSensorData(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description', 'measurement']

#
#
# class SensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ['name', 'description']
#
#
# class MeasurementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Measurement
#         fields = ['sensor', 'temp']
#
#
# class MeasurementSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Measurement
#         fields = ['temp', 'date']
#
#
# class SensorDetailSerializer(serializers.ModelSerializer):
#     measurement = MeasurementSerializer2(read_only=True, many=True)
#
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description', 'measurement']
#
# class SensorSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description']