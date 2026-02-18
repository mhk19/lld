from math import ceil
import time
from vehicle import Vehicle


class ParkingTicket:
    
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.start_time = time.time()

    def getTotalPrice(self):
        time_taken = ceil((time.time() - self.start_time)/60)
        unit_price = self.vehicle.getPerHourCharge()
        return time_taken*unit_price
        