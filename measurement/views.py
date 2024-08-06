from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.generics import CreateAPIView
from .serializers import  MeasurementSerializer, SensorSerializer
from .models import Sensor, Measurement

class SensorListCreateApiView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementCreateApiView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorRetrieveUpdateApiView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
