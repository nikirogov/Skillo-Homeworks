class vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start_engine(self):
        pass
class car(vehicle):
    def start_engine(self):
        return f"put keys in your:  {self.brand}"

class bicycle(vehicle):
    def start_engine(self):
        return f"start cycling your: {self.brand}"

vehicle1 = car("Toyota")
vehicle2 = bicycle("Kolelo")
print (vehicle1.start_engine())
print (vehicle2.start_engine())