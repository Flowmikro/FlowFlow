from django.contrib import admin
from .models import *


@admin.register(CarBuy)
class AdminCarBuy(admin.ModelAdmin):
    list_display = ['name', 'last_name']


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phonenum', 'car']