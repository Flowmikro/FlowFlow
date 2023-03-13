from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('cayman/', views.cayman, name='cayman'),
    path('911/', views.porsche911, name='911'),
    path('taycan/', views.taycan, name='taycan'),
    path('panamera/', views.panamera, name='panamera'),
    path('macan/', views.macan, name='macan'),
    path('cayenne/', views.cayenne, name='cayenne'),
    path('finser/', views.financial_services, name='fin_ser'),
    path('service/', views.service, name='service'),
    path('testdrive/', views.testdrive, name='testdrive'),
    path('finser/credit', views.credit, name='credit'),
    path('finser/credit/standard', views.standard, name='standard'),
    path('finser/credit/standard-used', views.standard_used, name='standard_used'),
    path('finser/credit/special-credit', views.special_credit, name='special_credit'),
    path('finser/insurance', views.insurance, name='insurance'),
    path('finser/leasing', views.leasing, name='leasing'),
    path('service/servicing', views.servicing, name='servicing'),
    path('service/seasonal-checks', views.seasonal_checks, name='seasonal_checks'),
    path('service/spares', views.spares, name='spares'),
    path('service/tequipment', views.tequipment, name='tequipment'),
    path('rights/', views.rights, name='rights'),
    path('data-processing-policy/', views.data_processing_policy, name='data_processing_policy'),
    path('contacts/', views.contacts, name='contacts'),
    # path('service/booking', views.booking, name='booking'),
]