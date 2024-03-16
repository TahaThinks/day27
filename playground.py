# Positional Argument
# def add(*args):
#     sum=0
#     for n in args:
#         sum += n
#     print(sum)
# add(1,2,3,4,5,6,7,8,9,10)


def calculate(value, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    value += kwargs["add"]
    value *= kwargs["multiply"]
    print(value)


calculate(5, add=3, multiply=5)