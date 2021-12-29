from django.contrib import admin

from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['id']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id_sensor', 'temp_dimension', 'date_dimension']
