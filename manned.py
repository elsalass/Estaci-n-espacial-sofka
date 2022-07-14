from spacecraft import Spacecraft

class Manned(Spacecraft):
    capacity = int
    active = bool
    distance = int

    def __init__(self, name, type, country, weight, fuel, activity, detail, power, capacity, active, distance):
        super().__init__(name, type, country, weight, fuel, activity, detail, power)
        self.capacity = capacity
        self.active = active
        self.distance = distance