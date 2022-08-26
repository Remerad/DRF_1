from rest_framework.routers import DefaultRouter
from .views import SensorsView, MeasurementView

router = DefaultRouter()
router.register('sensors', SensorsView, basename='Sensor')
router.register('measurement', MeasurementView, basename='Measurement')


urlpatterns = router.urls


# from django.urls import path
#
# from .views import oneSensorView, SensorsView, measurementsView
#
# urlpatterns = [
#     # TODO: зарегистрируйте необходимые маршруты
#     path('sensors/', SensorsView.as_view()),
#     #path('sensors/<pk>/', oneSensorView.as_view()),   #Данные одного датчика
#     # path('measurements/', measurementsView.as_view()),   #Данные датчика
# ]

