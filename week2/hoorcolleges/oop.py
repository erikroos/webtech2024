class Bike:
    # constructor
    def __init__(self, max_speed=20, is_electric=False):
        self._max_speed = max_speed
        self._is_electric = is_electric

    # print
    def __str__(self):
        return f"Deze fiets kan {self._max_speed} km/u en is {'wel' if self._is_electric else 'niet'} elektrisch"
    
    # equals
    def __eq__(self, other):
        if self._max_speed == other._max_speed and self._is_electric == other._is_electric:
            return True
        return False

    # getter en setter
    def get_max_speed(self):
        return self._max_speed
    
    def set_max_speed(self, new_max_speed):
        if new_max_speed > 0 and new_max_speed < 40:
            self._max_speed = new_max_speed
        else:
            print("Illegale waarde")

    max_speed = property(get_max_speed, set_max_speed)


bike = Bike(25, False)
print(bike)

bike2 = Bike(25, False)
print(bike2)

bike3 = bike2
print(bike3)

print(bike == bike2)
print(bike2 == bike3)

bike4 = Bike()
print(bike4)
bike4.max_speed = 140
print(bike4.max_speed)
bike4.max_speed = 30
print(bike4.max_speed)
print(bike4)