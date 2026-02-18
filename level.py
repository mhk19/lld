from parkingspot import ParkingSpot
from vehicle import VehicleType, Vehicle

class ParkingLevel:
    
    def __init__(self, level_number):
        self.level_number = level_number
        self.parking_spots = {str(VehicleType.CAR) : [], str(VehicleType.MOTORCYCLE) : [], str(VehicleType.TRUCK) : []}
    
    def addParkingSpots(self, number_of_spots, vehicle_type):
        newParkingSpots = [ParkingSpot(vehicle_type, self.level_number) for _ in number_of_spots]
        self.parking_spots.extend(newParkingSpots)
    
    def findParkingSpot(self, vehicle_type : VehicleType):
        parking_spots = self.parking_spots[str(vehicle_type)]
        available_spots = [parking_spot for parking_spot in parking_spots if parking_spot.isAvailable()]
        if not len(available_spots):
            return 0
        return available_spots[0]
    
    def park_vehicle(self, vehicle: Vehicle):
        parking_spot = self.findParkingSpot(vehicle.getVehicleType())
        if parking_spot == 0:
            return 0
        parking_spot.setTaken()
        return parking_spot
        
    def unpark_vehicle(self, vehicle: Vehicle):
        parking_spot = vehicle.getParkingSpot()
        if parking_spot:
            parking_spot.setAvailable()
