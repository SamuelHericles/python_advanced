"""
    Design pattern provide a way for create a objects without show logic.
    Implements a common interface for a new type object.
"""
from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """


class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1


# s1 = Student()
# s1.person_method()

# t1 = Teacher()
# t1.person_method()

if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()
