from rest_framework.decorators import api_view
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDataSerializer, MeasurementSerializer


@api_view(['POST'])
def create_sensor(request, title, description):
    Sensor(title=title, description=description).save()

    sensor = Sensor.objects.all()
    ser = SensorSerializer(sensor, many=True)
    return Response(ser.data[-1])


@api_view(['GET'])
def list_sensor(request):
    sensors = Sensor.objects.all()
    ser = SensorSerializer(sensors, many=True)
    return Response(ser.data)


@api_view(['GET'])
def sensor_data(request, sensor_id):
    sensor = Sensor.objects.get(id=sensor_id)
    ser = SensorDataSerializer(sensor, many=False)
    return Response(ser.data)


@api_view(['PATCH'])
def update_sensor(request, sensor_id, title=None, description=None):
    if title is None:
        Sensor(id=sensor_id, description=description).save()
    elif description is None:
        Sensor(id=sensor_id, title=title).save()
    elif title is None and description is None:
        return {'error': 'no data'}
    else:
        Sensor(id=sensor_id, title=title, description=description).save()

    sensor = Sensor.objects.get(id=sensor_id)
    ser = SensorDataSerializer(sensor, many=False)
    return Response(ser.data)


@api_view(['POST'])
def add_dimension(request, sensor_id, temperature):
    sensor = Sensor.objects.get(id=sensor_id)
    Measurement(id_sensor=sensor, temp_dimension=temperature).save()
    return Response({f'Датчик id={sensor_id}': f'Температура {temperature}'})
