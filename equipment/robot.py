
from .machine import Machine

class Robot(Machine):
    def __init__(self, name, temperature, power_kw, robot_type):
        super().__init__(name, temperature, power_kw)
        self.robot_type = robot_type

    def weld(self):
        if self.status == "Running":
            print(f"{self.name} is performing {self.robot_type} welding")
        else:
            print(f"{self.name} cannot weld because it is stopped")
    def paint(self):
        if self.status == "Running":
            print(f"{self.name} is performing {self.robot_type} Painting")
        else:
            print(f"{self.name} cannot Paint because it is stopped")