from django.urls import path

#from smart_home.measurement.views import demo
#rom measurement.views import SensorView, MeasurementView
from .views import allSensorView,  post_sensor, oneSensorView, postMeasurement, patchSensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', allSensorView.as_view()), #выводит все датчики
    path('sensors/<pk>', oneSensorView.as_view()),   #Данные одного датчика
    path('post/', post_sensor.as_view()),   #Создаёт датчик
    path('patch/<pk>', patchSensor.as_view()),  #Обновляет описание датчика

    path('measurements/', postMeasurement.as_view()),   #Данные датчика

]

