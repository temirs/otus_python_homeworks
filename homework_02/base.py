from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
                return self.started
            raise exceptions.LowFuelError

    def move(self):
        if self.fuel_consumption <= self.fuel:
            return True
        raise exceptions.NotEnoughFuel
