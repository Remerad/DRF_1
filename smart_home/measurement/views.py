# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
#from rest_framework import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from smart_home.measurement.models import Sensor
from smart_home.measurement.models import Measurement
from smart_home.measurement.serializers import SensorSerializer

# @api_view(['GET'])
# def demo(request):
#     data = {'message': 'hello'}
#     return Response(data)


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    def post(self, request):
        return Response({'status': 'ОК'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorSerializer
    def post(self, request):
        return Response({'status': 'ОК'})

class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAdminUser]