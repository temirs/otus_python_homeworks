"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base, exceptions


class Plane(base.Vehicle):
    cargo = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, quantity):
        if quantity + self.cargo > self.max_cargo:
            return exceptions.CargoOverload
        self.cargo += quantity


    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo
