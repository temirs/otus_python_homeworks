from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if Vehicle.started is False:
            if self.fuel > 0:
                Vehicle.started = True
            else:
                return exceptions.LowFuelError()

    def move(self, dist):
        if dist / self.fuel_consumption <= self.fuel:
            self.fuel -= (dist / self.fuel_consumption)
        else:
            return exceptions.NotEnoughFuel()
