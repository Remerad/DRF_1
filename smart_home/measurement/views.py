# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
#from rest_framework import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Sensor
from .models import Measurement
from .serializers import SensorSerializer, oneSensorData, MeasurementSerializer


# @api_view(['GET'])
# def demo(request):
#     data = {'message': 'hello'}
#     return Response(data)


class post_sensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class oneSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = oneSensorData


class allSensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class patchSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class postMeasurement(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
