from django.urls import path
from .views import *

urlpatterns = [
    path('petrol-stations/', PetrolStationListCreate.as_view(), name='petrolstation-list-create'),
    path('petrol-stations/<int:pk>/', PetrolStationDetail.as_view(), name='petrolstation-detail'),
    path('fuel-types/', FuelTypeListCreate.as_view(), name='fueltype-list-create'),
    path('fuel-types/<int:pk>/', FuelTypeDetail.as_view(), name='fueltype-detail'),
    path('fuel-prices/', FuelPriceListCreate.as_view(), name='fuelprice-list-create'),
    path('fuel-prices/<int:pk>/', FuelPriceDetail.as_view(), name='fuelprice-detail'),
    path('vehicles/', VehicleListCreate.as_view(), name='vehicle-list-create'),
    path('vehicles/<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),
    path('refuel-records/', RefuelRecordListCreate.as_view(), name='refuelrecord-list-create'),
    path('refuel-records/<int:pk>/', RefuelRecordDetail.as_view(), name='refuelrecord-detail'),
]