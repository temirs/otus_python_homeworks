"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


def LowFuelError():
    raise Exception('LowFuelError')


def NotEnoughFuel():
    raise Exception('NotEnoughFuel')


def CargoOverload():
    raise Exception('CargoOverload')
