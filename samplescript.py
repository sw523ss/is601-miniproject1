class Car(object):

    def factory(type):
        if type == "Sportscar":
            return Sportscar()
        if type == "Van":
            return Van()

    factory = staticmethod(factory)

class Sportscar(Car):
    def drive(self):
        print("Sportscar driving.")

class Van(Car):
    def drive(self):
        print("Van driving.")

# Create object using factory.
obj = Car.factory("Sportscar")
obj.drive()