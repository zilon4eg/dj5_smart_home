from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    description = models.CharField(max_length=300, blank=True, verbose_name='Описание')


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temp_dimension = models.FloatField(verbose_name='Температура')
    date_dimension = models.DateField(auto_now_add=True, verbose_name='Дата измерения')


