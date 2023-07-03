from abc import ABC

from engine.car import Car
from engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
