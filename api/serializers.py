from rest_framework import serializers
from PetrolStation.models import *

class PetrolStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetrolStation
        fields = '__all__'


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'


class FuelPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelPrice
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class RefuelRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefuelRecord
        fields = '__all__'
