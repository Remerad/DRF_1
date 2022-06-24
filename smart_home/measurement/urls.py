from django.urls import path

#from smart_home.measurement.views import demo
#rom measurement.views import SensorView, MeasurementView
from smart_home.measurement.views import SensorView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view()),
]
