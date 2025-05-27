# examples: car builder, HTTP request/ response builder, GSAP timeline builder

from car import CarBuilder

builder = CarBuilder()

car = builder.add_engine("V16").add_paint("red").add_wheels(4)

mycar = car.build()

print(mycar)