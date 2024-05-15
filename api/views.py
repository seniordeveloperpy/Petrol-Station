from rest_framework import generics
from PetrolStation.models import *
from .serializers import *

class PetrolStationListCreate(generics.ListCreateAPIView):
    queryset = PetrolStation.objects.all()
    serializer_class = PetrolStationSerializer

class PetrolStationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetrolStation.objects.all()
    serializer_class = PetrolStationSerializer

class FuelTypeListCreate(generics.ListCreateAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer

class FuelTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer

class FuelPriceListCreate(generics.ListCreateAPIView):
    queryset = FuelPrice.objects.all()
    serializer_class = FuelPriceSerializer

class FuelPriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FuelPrice.objects.all()
    serializer_class = FuelPriceSerializer

class VehicleListCreate(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class RefuelRecordListCreate(generics.ListCreateAPIView):
    queryset = RefuelRecord.objects.all()
    serializer_class = RefuelRecordSerializer

class RefuelRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RefuelRecord.objects.all()
    serializer_class = RefuelRecordSerializer



