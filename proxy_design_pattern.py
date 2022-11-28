"""
    This design pattern provide a surrogate or placeholder for
    another object to control access to it. When used for provide controled 
    access of a functionality.
"""

from abc import ABCMeta, abstractclassmethod


class IPerson(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method():
        """ Interface Method """


class Person(IPerson):

    def person_method(self):
        print("I am a person!")


class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy funcitonality!")
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
