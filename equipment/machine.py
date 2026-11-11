
class Machine:
    def __init__(self, name, temperature, power_kw):
        self.name = name
        self.temperature = temperature
        self.power_kw = power_kw
        self.status = "Stopped"

    def start(self):
        self.status = "Running"
        print(f"{self.name} has started")

    def stop(self):
        self.status = "Stopped"
        print(f"{self.name} has stopped")

    def check_status(self):
        print(f"{self.name} status: {self.status}")
    def show_temperature(self):
        print(f"{self.name} temperature: {self.temperature}°C")
