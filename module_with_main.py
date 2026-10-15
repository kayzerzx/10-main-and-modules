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

def main():
    print("Just testing")
    print(area(7))
    print(pi)
    #every python file (aka module) has a special built in variable called __name__
    #if you run file directly, __nane__ is set to "__main__"
    #if you import file, __name__ becomes the name of that script
    print(__name__)
    print("Just testing")

if __name__ == "__main__":
    main()
