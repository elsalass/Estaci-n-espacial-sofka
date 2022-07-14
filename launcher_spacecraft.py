from spacecraft import Spacecraft

class Launcher_spacecraft(Spacecraft):
    height = int
    load_weight = int
    
    def __init__(self, name, type, country, weight, fuel, activity, detail, power, height, load_weight):
        super().__init__(name, type, country, weight, fuel, activity, detail, power)
        self.height = height
        self.load_weight = load_weight
