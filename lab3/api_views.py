from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer
import csv
import io

@api_view(['GET'])
def sensor_list(request):
    sensors = SensorData.objects.all()
    serializer = SensorDataSerializer(sensors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sensor_detail(request, pk):
    try:
        sensor = SensorData.objects.get(pk=pk)
    except SensorData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SensorDataSerializer(sensor)
    return Response(serializer.data)

@api_view(['GET'])
def sensors_by_location(request, location):
    sensors = SensorData.objects.filter(location=location)
    serializer = SensorDataSerializer(sensors, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def sensor_create(request):
    serializer = SensorDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES['file']
    if not file.name.endswith('.csv'):
        return Response({'error': 'File is not CSV type'}, status=status.HTTP_400_BAD_REQUEST)
    
    data_set = file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)  # пропустити заголовок
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = SensorData.objects.update_or_create(
            location=column[0],
            measurement_date=column[1],
            measurement_time=column[2],
            temperature=column[3],
            sensor_name=column[4],
            sensor_model=column[5],
            sensor_group=column[6],
            pressure=column[7],
            co2_level=column[8]
        )
    return Response({'status': 'CSV file uploaded successfully'}, status=status.HTTP_201_CREATED)
