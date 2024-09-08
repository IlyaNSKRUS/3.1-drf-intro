# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorCreateSerializer, MeasurementCreateSerializer, \
    SensorDetailSerializer, MeasurementSerializer


class SensorsViewCreate(ListCreateAPIView): # Просмотр всех датчиков; Создание датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        ser = SensorCreateSerializer(data=request.data)
        print(ser.is_valid())
        ser.is_valid()
        ser.save()
        return Response(request.data)

class SensorViewUpdate(RetrieveUpdateAPIView):  # Обновление датчика; Просмотр деталей датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsCreate(CreateAPIView):    # Создание показаний
    def post(self, request):
        ser = MeasurementCreateSerializer(data=request.data)
        ser.is_valid()
        ser.save()
        return Response(request.data)
