from django.db import models

class PetrolStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    start_work = models.DateTimeField()
    end_work = models.DateTimeField()

    def __str__(self):
        return self.name
    

class FuelType(models.Model):
    PETROL = 'P'
    GAS = 'G'
    ELECTRIC = 'E'

    FUEl_ChOICES = [
        (PETROL, 'Petrol'),
        (GAS, 'Gas'),
        (ELECTRIC, 'Electric'),
    ]

    name = models.CharField(max_length=1, choices=FUEl_ChOICES, unique=True)

    def __str__(self):
        return self.get_name_display()
    

class FuelPrice(models.Model):
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.fuel_type.get_name_display()} - {self.price_per_unit} per unit"
    

class Vehicle(models.Model):
    petrol_station = models.ForeignKey(PetrolStation, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"{self.vehicle_type} {self.license_plate}"
    

class RefuelRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    paid_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Refuel {self.vehicle.license_plate} - {self.amount} units"