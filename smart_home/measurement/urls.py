from django.urls import path

from measurement.views import SensorsViewCreate, SensorViewUpdate, MeasurementsCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsViewCreate.as_view()),
    path('sensors/<pk>/', SensorViewUpdate.as_view()),
    path('measurements/', MeasurementsCreate.as_view()),
]
