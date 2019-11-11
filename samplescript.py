class Flounder:
    fish = ""

    # default constructor
    def __init__(self):
        self.fish = "Flounder"

    # a method for printing data members
    def print_Fish(self):
        print(self.fish)

    # creating object of the class

obj = Flounder()

    # calling the instance method using the object obj

obj.print_Fish()