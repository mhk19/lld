from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3


class Vehicle(ABC):

    def __init__(self, number):
        self.number = number
    
    @abstractmethod
    def getVehicleType():
        pass
    
    def getVehicleNumber(self):
        return self.number
    
    @abstractmethod
    def getPerHourCharge():
        pass
    
    def setParkingSpot(self, parking_spot):
        self.parking_spot = parking_spot
        
    def getParkingSpot(self):
        if self.parking_spot:
            return self.parking_spot
        return 0
    
class Car(Vehicle):
    
    def __init__(self, number):
        super().__init__(number)
    
    def getVehicleType(self):
        return VehicleType.CAR
    
    def getPerHourCharge():
        return 50


class Motorcycle(Vehicle):
    
    def __init__(self, number):
        super().__init__(number)
    
    def getVehicleType(self):
        return VehicleType.MOTORCYCLE

    def getPerHourCharge():
        return 30
    
class Truck(Vehicle):
    
    def __init__(self, number):
        super().__init__(number)
    
    def getVehicleType(self):
        return VehicleType.TRUCK
    
    def getPerHourCharge():
        return 100
