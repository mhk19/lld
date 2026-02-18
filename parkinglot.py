from level import ParkingLevel


class ParkingLot:
    
    def __init__(self):
        self.levels = []
    
    def add_level(self):
        number_of_levels = len(self.levels)
        new_level = ParkingLevel(number_of_levels+1)
        return new_level
