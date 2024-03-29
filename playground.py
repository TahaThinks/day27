# Positional Argument
# def add(*args):
#     sum=0
#     for n in args:
#         sum += n
#     print(sum)
# add(1,2,3,4,5,6,7,8,9,10)

# Keyword Argument
# def calculate(value, **kwargs):
#     # print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key, value)
#     value += kwargs["add"]
#     value *= kwargs["multiply"]
#     print(value)
#
#
# calculate(5, add=3, multiply=5)

# Class using Keyword Argument
# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.year = kwargs.get("year")
#
#     def car_info(self):
#         print(f"Car is {self.make} {self.model}")
#
#
# my_car = Car(make="BMW", model="X3", year=2022)
# my_car.car_info()
#
# my_new_car = Car(make="Nissan")
# my_new_car.car_info()