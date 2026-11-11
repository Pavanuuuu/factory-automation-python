
from .machine import Machine

class Conveyor(Machine):
    def __init__(self, name, temperature, power_kw, speed):
        super().__init__(name, temperature, power_kw)
        self.speed = speed

    def move_products(self):
        if self.status == "Running":
            print(f"{self.name} is moving products at {self.speed} m/s")
        else:
            print(f"{self.name} cannot move products because it is stopped")
