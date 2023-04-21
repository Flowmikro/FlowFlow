from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', cache_page(60*8)(views.homepage), name='home'),
    path('cayman/',  cache_page(60*8)(views.cayman), name='cayman'),
    path('911/',  cache_page(60*8)(views.porsche911), name='911'),
    path('taycan/',  cache_page(60*8)(views.taycan), name='taycan'),
    path('panamera/',  cache_page(60*8)(views.panamera), name='panamera'),
    path('macan/',  cache_page(60*8)(views.macan), name='macan'),
    path('cayenne/',  cache_page(60*8)(views.cayenne), name='cayenne'),
    path('finser/', cache_page(60*8)(views.financial_services), name='fin_ser'),
    path('service/', cache_page(60*8)(views.service), name='service'),
    path('testdrive/', cache_page(60*8)(views.testdrive), name='testdrive'),
    path('finser/credit',  cache_page(60*8)(views.credit), name='credit'),
    path('finser/credit/standard', cache_page(60*8)(views.standard), name='standard'),
    path('finser/credit/standard-used', cache_page(60*8)(views.standard_used), name='standard_used'),
    path('finser/credit/special-credit', cache_page(60*8)(views.special_credit), name='special_credit'),
    path('finser/insurance', cache_page(60*8)(views.insurance), name='insurance'),
    path('finser/leasing', cache_page(60*8)(views.leasing), name='leasing'),
    path('service/servicing', cache_page(60*8)(views.servicing), name='servicing'),
    path('service/seasonal-checks',  cache_page(60*8)(views.seasonal_checks), name='seasonal_checks'),
    path('service/spares', cache_page(60*8)(views.spares), name='spares'),
    path('service/tequipment', cache_page(60*8)(views.tequipment), name='tequipment'),
    path('rights/', cache_page(60*8)(views.rights), name='rights'),
    path('data-processing-policy/', cache_page(60*8)(views.data_processing_policy), name='data_processing_policy'),
    path('contacts/', cache_page(60*8)(views.contacts), name='contacts'),
]