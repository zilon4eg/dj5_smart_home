from django.urls import path
from django.contrib import admin

from measurement.views import add_dimension, create_sensor, list_sensor, update_sensor, sensor_data


urlpatterns = [
    path('create_sensor/<title>/<description>/', create_sensor),
    path('list_sensor/', list_sensor),
    path('sensor_data/id=<sensor_id>/', sensor_data),
    path('update_sensor/<sensor_id>/<title>/<description>/', update_sensor),
    path('add_dimension/id=<sensor_id>/temp=<temperature>/', add_dimension),
]
