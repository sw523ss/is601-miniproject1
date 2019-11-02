class Car(object):

    def __init__(self):
        self._types = [Type('front_left'),
                             Type('front_right'),
                             Type('rear_left'),
                             Type('rear_right'), ]
        self._tank = Tank(70)

    def types_pressure(self):
        return [type.pressure for type in self._types]

    def fuel_level(self):
        return self._tank.level
