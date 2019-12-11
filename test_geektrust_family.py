'''
Description: This class contains the unit test methods 
to test all the get relationship, add child and add spouse 
methods required by the problem. 
For most functions, positive and negative test cases have been added
'''

import unittest
import sys
from person import Person
from main_class import MainClass

# Constants defined here
MALE = "Male"
FEMALE = "Female"
POPULATE_FAMILY_TREE_FILE = "Inputs/Populate_Family_Tree.txt"

class TestFamily(unittest.TestCase):
    # Function to first contruct the family tree and store the root as Shan
    def setUp(self):
        main_class = MainClass()
        self.shan = Person("Shan", MALE)
        self.obj = Person()
        commands = main_class.read_input_file(POPULATE_FAMILY_TREE_FILE)
        main_class.call_fam_funcs(self.shan, commands, populate_family_tree=True)
    
    def test_find_person_positive(self):
        answers_retrieved_obj = self.obj.find_person(self.shan, "Kriya")
        self.assertEqual( "Kriya", answers_retrieved_obj.name)
        
    def test_find_person_negative(self):
        answers_retrieved_obj = self.obj.find_person(self.shan, "abc")
        self.assertEqual( None, answers_retrieved_obj)

    def test_paternal_uncles_positive(self):
        correct_answer = ['Chit', 'Ish', 'Vich']
        answers_retrieved_obj = self.obj.get_paternal_uncles(self.shan, "Jnki")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_paternal_uncles_negative_none(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_paternal_uncles(self.shan, "Satvy")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_maternal_uncles_positive(self):
        correct_answer = ['Ahit']
        answers_retrieved_obj = self.obj.get_maternal_uncles(self.shan, "Lavnya")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_maternal_uncles_negative_none(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_maternal_uncles(self.shan, "Vila")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_paternal_aunts_positive(self):
        correct_answer = ['Atya']
        answers_retrieved_obj = self.obj.get_paternal_aunts(self.shan, "Vasa")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_paternal_aunts_negative_none(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_paternal_aunts(self.shan, "Krpi")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_maternal_aunts_positive(self):
        correct_answer = ['Tritha']
        answers_retrieved_obj = self.obj.get_maternal_aunts(self.shan, "Yodhan")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_maternal_aunts_negative_none(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_maternal_aunts(self.shan, "Krithi")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_sisters_in_laws_positive(self):
        correct_answer = ['Amba', 'Lika', 'Chitra']
        answers_retrieved_obj = self.obj.get_sisters_in_law(self.shan, "Satya")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_sisters_in_laws_negative_none(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_sisters_in_law(self.shan, "Jnki")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_brothers_in_laws_positive(self):
        correct_answer = ['Ahit']
        answers_retrieved_obj = self.obj.get_brothers_in_law(self.shan, "Arit")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_brothers_in_laws_negative_none(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_brothers_in_law(self.shan, "Chika")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_sons_positive(self):
        correct_answer = ['Chit', 'Ish', 'Vich', 'Aras']
        answers_retrieved_obj = self.obj.get_sons(self.shan, "Anga")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_sons_negative(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_sons(self.shan, "Vich")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_daughters_positive(self):
        correct_answer = ['Dritha', 'Tritha']
        answers_retrieved_obj = self.obj.get_daughters(self.shan, "Chit")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_daughters_negative(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_daughters(self.shan, "Asva")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_siblings_positive(self):
        correct_answer = ['Chit', 'Ish', 'Aras', 'Satya']
        answers_retrieved_obj = self.obj.get_siblings(self.shan, "Vich")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_siblings_negative(self):
        correct_answer = 0
        answers_retrieved_obj = self.obj.get_siblings(self.shan, "Jaya")
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_brothers_positive(self):
        correct_answer = ['Chit', 'Ish', 'Vich', 'Aras']
        person = self.obj.find_person(self.shan, "Satya")
        answers_retrieved_obj = self.obj.get_brothers(person)
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_brothers_negative(self):
        correct_answer = 0
        person = self.obj.find_person(self.shan, "Yodhan")
        answers_retrieved_obj = self.obj.get_brothers(person)
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_sisters_positive(self):
        correct_answer = ['Dritha', 'Tritha']
        person = self.obj.find_person(self.shan, "Vritha")
        answers_retrieved_obj = self.obj.get_sisters(person)
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_sisters_negative(self):
        correct_answer = 0
        person = self.obj.find_person(self.shan, "Lavnya")
        answers_retrieved_obj = self.obj.get_sisters(person)
        self.assertEqual( len(answers_retrieved_obj), correct_answer)

    def test_add_child_daughter(self):
        mother = self.obj.find_person(self.shan, "Jnki")
        self.obj.add_child(mother, Person("Rohini", FEMALE))
        correct_answer = ["Lavnya", "Rohini"]
        answers_retrieved_obj = self.obj.get_daughters(self.shan, "Jnki")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)
        father = self.obj.find_person(self.shan, "Arit")
        answers_retrieved_obj = self.obj.get_daughters(self.shan, father.wife.name)
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_add_child_son(self):
        mother = self.obj.find_person(self.shan, "Dritha")
        self.obj.add_child(mother, Person("Arjun", MALE))
        correct_answer = ["Yodhan", "Arjun"]
        answers_retrieved_obj = self.obj.get_sons(self.shan, "Dritha")
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)
        father = self.obj.find_person(self.shan, "Jaya")
        answers_retrieved_obj = self.obj.get_sons(self.shan, father.wife.name)
        answers_retrieved_lst = list()
        for answer in answers_retrieved_obj:
            answers_retrieved_lst.append(answer.name) 
        self.assertEqual( answers_retrieved_lst, correct_answer)

    def test_add_spouse_husband(self):
        wife = self.obj.find_person(self.shan, "Chika")
        husband_to_be_added = Person("Chetan", MALE)
        self.obj.add_spouse(wife, husband_to_be_added)
        husband = self.obj.find_person(self.shan, "Chetan")
        self.assertEqual( husband.name, "Chetan")

    def test_add_spouse_wife(self):
        husband = self.obj.find_person(self.shan, "Ahit")
        wife_to_be_added = Person("Deepa", FEMALE)
        self.obj.add_spouse(husband, wife_to_be_added)
        wife = self.obj.find_person(self.shan, "Deepa")
        self.assertEqual( wife.name, "Deepa")
        

if __name__ == '__main__':
    unittest.main()