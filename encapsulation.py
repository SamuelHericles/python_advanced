"""
    wrapping variables and methods for together as a single unit.
"""


class Person:

    def __init__(self, name, age, gender):

        # Privavte variabels, cannot make gettters and setters
        self.__name = name
        self.__age = age
        self.__gender = gender

    # Getter
    @property
    def Name(self):
        return  self.__name

    # Sttter
    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value

    @staticmethod
    def mymethod():
        print("Hello World!")


Person.mymethod()

p1 = Person("Mike", 20, 'm')
print(p1.Name)

p1.Name = 'Bob'
print(p1.Name)
