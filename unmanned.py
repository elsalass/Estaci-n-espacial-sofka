from xmlrpc.client import boolean
from spacecraft import Spacecraft

class Unmanned(Spacecraft):
    study_objectiv = str
    active = bool

    def __init__(self, name, type, country, weight, fuel, activity, detail, power, study_objectiv, active):
        super().__init__(name, type, country, weight, fuel, activity, detail, power)
        self.study_objectiv = study_objectiv
        self.active = active
