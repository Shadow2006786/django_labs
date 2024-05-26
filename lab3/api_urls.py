from django.urls import path
from . import api_views

urlpatterns = [
    path('sensors/', api_views.sensor_list, name='sensor-list'),
    path('sensors/<int:pk>/', api_views.sensor_detail, name='sensor-detail'),
    path('sensors/location/<str:location>/', api_views.sensors_by_location, name='sensors-by-location'),
    path('sensors/create/', api_views.sensor_create, name='sensor-create'),
    path('sensors/upload_csv/', api_views.upload_csv, name='upload-csv'),
]
