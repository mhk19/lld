class ParkingSpot:
    
    def __init__(self, vehicle_type, level):
        self.vehicle_type = vehicle_type
        self.level = level
        self.is_available = True
        
    def setAvailable(self):
        self.is_available = True
    
    def setTaken(self):
        self.is_available = False
        
    def isAvailable(self):
        return self.is_available
