"""
    Using decorator for change the behavior function 
    without modifying the function itself.
"""
# --------------------------------------------------
# This is the basic ideia about decoretors
import time


def mydecorator(function):
    def wrapper():
        print("I am decorating your function!")
        function()

    return wrapper


def hello_world():
    print("Hello World")
# mydecorator(hello_world)()
# --------------------------------------------------

# Now using a decorator function


@mydecorator
def hello_world():
    print("Hello World")


# hello_world()

# --------------------------------------------------
# You cannot put a argument in hello function because the mydecorator wrapper haven't


@mydecorator
def hello(person):
    print(f"Hello {person}")


# hello('Mike') -> get a error
# --------------------------------------------------
# Solution: put args and kwargs
def mydecorator(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        return function(*args, **kwargs)
    return wrapper


@mydecorator
def hello(person):
    print(f"Hello {person}")
    return f"Hello {person}"


# print(hello('Mike'))

# --------------------------------------------------
# Pratical Example #1 - Logging
# This a example why the decorator is useful

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f'{fname} returned value {value}')
            f.write(f"{fname} returned value {value}\n")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


#print(add(1, 2))


# --------------------------------------------------
# Pratical Example #2 - Timing
# This example show how fast is using decorators

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute!")
    return wrapper  # Need for to execute the wrapper function


@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


myfunction(90000)
