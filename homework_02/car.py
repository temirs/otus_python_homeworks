"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base
from homework_02.engine import Engine


class Car(base.Vehicle):
    engine: Engine

    def set_engine(self, engine: Engine):
        self.engine = engine
