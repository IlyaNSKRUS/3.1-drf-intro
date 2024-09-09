from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    time_measurement = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo/%y/%m/%d', blank=True)



