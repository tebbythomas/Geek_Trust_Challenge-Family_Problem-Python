'''
Description: This class contains the relevant attributes of a person
'''

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.mother = None
        self.father = None
        self.children = list()
        self.wife = None
        self.husband = None