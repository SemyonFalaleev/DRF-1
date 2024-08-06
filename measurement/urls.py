from django.urls import path
from .views import  MeasurementCreateApiView, SensorListCreateApiView
from .views import SensorRetrieveUpdateApiView
urlpatterns = [
    path('sensors/', SensorListCreateApiView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateApiView.as_view()),
    path('measurements/', MeasurementCreateApiView.as_view()),
]
