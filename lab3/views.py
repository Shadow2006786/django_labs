from django.shortcuts import redirect, render, get_object_or_404
from .models import SensorData
from django.contrib.auth.decorators import login_required
import csv

from django import forms
from .forms import CSVUploadForm, SensorDataForm

@login_required
def secure_page(request):
    return render(request, 'secure.html')

@login_required
def upload_csv_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                SensorData.objects.create(
                    location=row['location'],
                    measurement_date=row['measurement_date'],
                    measurement_time=row['measurement_time'],
                    temperature=row['temperature'],
                    sensor_name=row['sensor_name'],
                    sensor_model=row['sensor_model'],
                    sensor_group=row['sensor_group'],
                    pressure=row['pressure'],
                    co2_level=row['co2_level'],
                )
            return redirect('upload-csv-success')
    else:
        form = CSVUploadForm()
    return render(request, 'upload_csv.html', {'form': form})

@login_required
def upload_csv_success_view(request):
    return render(request, 'upload_csv_success.html')


def sensor_list(request):
    sensors = SensorData.objects.all()
    return render(request, 'sensor_list.html', {'sensors': sensors})

def sensor_detail(request, sensor_id):
    sensor = get_object_or_404(SensorData, id=sensor_id)
    return render(request, 'sensor_detail.html', {'sensor': sensor})

def add_sensor(request):
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorDataForm()
    return render(request, 'add_sensor.html', {'form': form})
