# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorsView(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

#
# class SensorsView(APIView):
#     def get(self, request):
#         queryset = Sensor.objects.all()
#         serializer_class = SensorSerializer(queryset, many=True)
#         return Response(serializer_class.data)
#
#     def post(self, request):
#         sensorData = request.data
#         new_sensor = Sensor.objects.create(
#             id=sensorData['id'],
#             title=sensorData['title'],
#             description=sensorData['description']
#         )
#         new_sensor.save()
#         serializer_class = SensorSerializer(new_sensor)
#         return Response(serializer_class.data)
#
#
# class oneSensorView(APIView):
#     def get(self, request, pk):
#         queryset = Sensor.objects.all().filter(pk = pk)
#         serializer_class = SensorSerializer(queryset, many=True)
#         return Response(serializer_class.data)
#
#     def patch(self, request, pk):
#         targetSensor = Sensor.objects.all().filter(pk = pk).update(data = request.data)
#         updatedSensor = Sensor.objects.get(pk = pk)
#         serializer_class = SensorSerializer(targetSensor, many=True)
#         return Response(serializer_class.data)
#
#
# class measurementsView(APIView):
#     def post(self, request):
#         measurementData = request.data
#         new_measurement = Sensor.objects.create(
#             sensor=measurementData['sensor'],
#             temperature=measurementData['temperature']
#         )
#         new_measurement.save()
#         serializer_class = MeasurementSerializer(new_measurement)
#         return Response(serializer_class.data)