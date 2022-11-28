""""Special methods are start and end with underscore.
    They are also called dunder methods. Are good when not need 
    create a function for invocate something that is common in python."""

from __future__ import annotations


class Person:

    # specify constructor classes
    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age

    # Destroy objcted when this classe not used more, automatically. Finished the program.
    def __del__(self) -> None:
        print("Object is being desconstructed!")


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # When you add two or more classe values with + operator, you define with __add__ to do something.
    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    # def __str__ -> typecast or representation when the class was called in print

    # this diff in __str__ is __repr__ returns a 'official' output format. The __str__ your output is more human frendly.
    def __repr__(self) -> str:
        return f"X:{self.x}, Y:{self.y}"

    # when you call len built in function, she returns the lenght is 10.
    # def __len__(self):
    #     return 10

    def __call__(self):
        print("Hello World! This is a vector class!")


#p = Person("Mike", 25)
v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2

print(v3)
# print(len(v1))
v2()
