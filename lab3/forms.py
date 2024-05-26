from django import forms
from .models import SensorData
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class CSVUploadForm(forms.Form):
    file = forms.FileField()
    
class SensorDataForm(forms.ModelForm):
    class Meta:
        model = SensorData
        fields = ['location', 'measurement_date', 'measurement_time', 'temperature', 'sensor_name', 'sensor_model', 'sensor_group', 'pressure', 'co2_level']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'measurement_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'measurement_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
            'sensor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sensor_model': forms.TextInput(attrs={'class': 'form-control'}),
            'sensor_group': forms.TextInput(attrs={'class': 'form-control'}),
            'pressure': forms.NumberInput(attrs={'class': 'form-control'}),
            'co2_level': forms.NumberInput(attrs={'class': 'form-control'}),
        }