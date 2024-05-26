from django.db import models

class SensorData(models.Model):
    location = models.CharField(max_length=100)
    measurement_date = models.DateField()
    measurement_time = models.TimeField()
    temperature = models.FloatField()
    sensor_name = models.CharField(max_length=100)
    sensor_model = models.CharField(max_length=100)
    sensor_group = models.CharField(max_length=100)
    pressure = models.FloatField()  
    co2_level = models.FloatField()  

    def __str__(self):
        return f"{self.sensor_name} at {self.location} on {self.measurement_date} {self.measurement_time}"