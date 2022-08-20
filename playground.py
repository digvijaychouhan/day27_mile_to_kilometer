def add(*args):
    print(type(args))
    sum_of = 0
    for num in args:
        sum_of += num
    return sum_of


print(add(2, 3, 4, 5, 6, 7))


def calculate(**kwargs):
    print(kwargs)
    n = 0
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(add=3, multiply=5))
