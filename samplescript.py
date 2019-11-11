class Greeting:

    def __init__(self):
        pass

    def printhello(self, name):
        print(f"Hello, {name}")
        return name

obj=Greeting()
obj.printhello('John')