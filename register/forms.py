from .models import *
from django.forms import ModelForm


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'last_name', 'phonenum', 'car', 'comm']


class CarByuForm(ModelForm):
    class Meta:
        model = CarBuy
        fields = ['name', 'last_name', 'phonenum', 'car', 'email']