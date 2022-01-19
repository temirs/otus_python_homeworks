from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not Vehicle.started:
            if self.fuel > 0:
                Vehicle.started = True
            else:
                return exceptions.LowFuelError

    def move(self, dist):
        if dist / self.fuel_consumption <= self.fuel:
            self.fuel -= (dist / self.fuel_consumption)
        else:
            return exceptions.NotEnoughFuel
