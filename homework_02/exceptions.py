"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    raise Exception('LowFuelError')


class NotEnoughFuel(Exception):
    raise Exception('NotEnoughFuel')


class CargoOverload(Exception):
    raise Exception('CargoOverload')
