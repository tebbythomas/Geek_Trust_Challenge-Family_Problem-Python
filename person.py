'''
Description: This class contains the relevant attributes of a person.
It also contains the functions / relationships associated with a person
'''

# Constants defined here
MALE = "Male"
FEMALE = "Female"

class Person:
    def __init__(self, name=None, gender=None):
        self.name = name
        self.gender = gender
        self.mother = None
        self.father = None
        self.children = list()
        self.wife = None
        self.husband = None

    # Adds child to both the mother and the father           
    def add_child(self, mother, child):
        curr_children = mother.children
        curr_children.append(child)
        mother.children = curr_children
        mother.husband.children = mother.children
        child.mother = mother
        child.father = mother.husband

    # Adds the new spouse relationship to both partners
    def add_spouse(self, person, new_spouse):
        if new_spouse.gender == FEMALE:
            person.wife = new_spouse
            new_spouse.husband = person
        elif new_spouse.gender == MALE:
            person.husband = new_spouse
            new_spouse.wife = person

    # Helper function to find the relevant person object given just the name of the person
    def find_person(self, curr, person):
        if curr.name == person:
            return curr
        else:
            if curr.husband is not None:
                if curr.husband.name == person:
                    return curr.husband
            if curr.wife is not None:
                if curr.wife.name == person:
                    return curr.wife
            if len(curr.children) > 0:
                for child in curr.children:
                    ret_val = self.find_person(child, person)
                    if ret_val is not None:
                        return ret_val
        return None
    
    # Function takes Shan as a param to first find the relevant person object
    def get_sons(self, shan, person):
        person = self.find_person(shan, person)
        sons = list()
        for child in person.children:
            if child.gender == MALE:
                sons.append(child)
        return sons
    
    def get_daughters(self, shan, person):
        person = self.find_person(shan, person)
        daughters = list()
        for child in person.children:
            if child.gender == FEMALE:
                daughters.append(child)
        return daughters

    def get_siblings(self, shan, person):
        person = self.find_person(shan, person)
        siblings = list()
        mother = person.mother
        if mother is not None:
            for child in mother.children:
                if child.name != person.name :
                    siblings.append(child)
        return siblings

    def get_brothers(self, person):
        brothers = list()
        mother = person.mother
        if mother is not None:
            for child in mother.children:
                if child.name != person.name and child.gender == MALE:
                    brothers.append(child)
        return brothers

    def get_sisters(self, person):
        sisters = list()
        mother = person.mother
        if mother is not None:
            for child in mother.children:
                if child.name != person.name and child.gender == FEMALE:
                    sisters.append(child)
        return sisters

    def get_paternal_uncles(self, shan, person):
        person = self.find_person(shan, person)
        uncles = list()
        father = person.father
        if father is not None:
            uncles = self.get_brothers(father)
        return uncles

    def get_maternal_uncles(self, shan, person):
        person = self.find_person(shan, person)
        uncles = list()
        mother = person.mother
        if mother is not None:
            uncles = self.get_brothers(mother)
        return uncles

    def get_paternal_aunts(self, shan, person):
        person = self.find_person(shan, person)
        aunts = list()
        father = person.father
        if father is not None:
            aunts = self.get_sisters(father)
        return aunts
    
    def get_maternal_aunts(self, shan, person):
        person = self.find_person(shan, person)
        aunts = list()
        mother = person.mother
        if mother is not None:
            aunts = self.get_sisters(mother)
        return aunts

    def get_sisters_in_law(self, shan, person):
        person = self.find_person(shan, person)
        sisters_in_law = list()
        spouse = None
        if person.husband is not None:
            spouse = person.husband
        elif person.wife is not None:
            spouse = person.wife
        if spouse is not None:
            sisters_in_law = self.get_sisters(spouse)
        brothers = self.get_brothers(person)
        for brother in brothers:
            if brother.wife is not None:
                sisters_in_law.append(brother.wife)
        return sisters_in_law

    def get_brothers_in_law(self, shan, person):
        person = self.find_person(shan, person)
        brothers_in_law = list()
        spouse = None
        if person.husband is not None:
            spouse = person.husband
        elif person.wife is not None:
            spouse = person.wife
        if spouse is not None:
            brothers_in_law = self.get_brothers(spouse)
        sisters = self.get_sisters(person)
        for sister in sisters:
            if sister.husband is not None:
                brothers_in_law.append(sister.husband)
        return brothers_in_law