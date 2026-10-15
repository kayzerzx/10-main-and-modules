pi = 3.14159
def square(x):
    return x ** 2 

def cude(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius:float) -> float:
    """
    take the radious of a cricle and returns the area
    """
    return pi * (radius ** 2)