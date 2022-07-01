from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)   #описание (необязательное, например, "спальня" или "корридор на 2 этаже")


class Measurement(models.Model):
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField()
    date = models.DateField(auto_now_add=True)