class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Built a car with {self.engine} engine, {self.wheels} wheels, and {self.color} color"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_engine(self, model):
        self.car.engine = model
        return self

    def add_wheels(self, number):
        self.car.wheels = number
        return self

    def add_paint(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car
