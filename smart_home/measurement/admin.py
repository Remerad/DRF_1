from django.contrib import admin

# Register your models here.
from .models import Sensor, Measurement

admin.site.register(Sensor)
admin.site.register(Measurement)