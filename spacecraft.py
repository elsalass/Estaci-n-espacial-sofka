class Spacecraft:
    id = int
    name = str
    type   = str
    country   = str
    weight = int 
    fuel = str
    activity = range
    detail = str
    power = float

    def __init__(self, name, type, country, weight, fuel, activity, detail, power):
        self.name = name 
        self.country = country
        self.weight = weight
        self.type = type
        self.fuel = fuel
        self.activity = activity
        self.detail = detail
        self.power = power 