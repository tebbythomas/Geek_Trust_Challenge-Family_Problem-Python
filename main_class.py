'''
Description: This class handles the following important functions:
1. Parsing the input file containing the commands
2. Interpreting the commands and sending it to the relevant functions 
to be implemented
3. Prints the output to the terminal / console
'''

from person import Person

# Constants defined here
MALE = "Male"
FEMALE = "Female"


class MainClass:
    #
    def family_function_mapping(self, person_obj=None, text=None, param1=None, param2=None, param3=None):
        # Dictionary mapping relationship text with function name
        if text == "ADD_SPOUSE": 
            return person_obj.add_spouse(param1, Person(param2, param3))
        elif text == "ADD_CHILD": 
            return person_obj.add_child(param1, Person(param2, param3))
        elif text == "Paternal-Uncle":
            return person_obj.get_paternal_uncles(param1, param2)
        elif text == "Maternal-Uncle":
             return person_obj.get_maternal_uncles(param1, param2)
        elif text == "Paternal-Aunt":
            return person_obj.get_paternal_aunts(param1, param2)
        elif text == "Maternal-Aunt": 
            return person_obj.get_maternal_aunts(param1, param2)
        elif text == "Sister-In-Law":
            return person_obj.get_sisters_in_law(param1, param2)
        elif text == "Brother-In-Law":
            return person_obj.get_brothers_in_law(param1, param2)
        elif text == "Son":
            return person_obj.get_sons(param1, param2)
        elif text == "Daughter":
            return person_obj.get_daughters(param1, param2)
        elif text == "Siblings":
            return person_obj.get_siblings(param1, param2)
        else:
            print("Incorrect Relationship specified")
            exit(0)
        return None

    # Parses the input file    
    def read_input_file(self, input_file):
        f = open(input_file)
        commands = list()
        for line in f:
            commands.append(line.strip("\n").split(" "))
        f.close()
        return commands

    # Interprets the commands in each file
    def call_fam_funcs(self, shan, commands, populate_family_tree=False):
        # Object to call methods of Class Family_Functions
        obj = Person()
        for command in commands:
            output = list()
            # Commands can be basically of 2 types: Add_CHILD and GET_RELATIONSHIP
            if command[0] == "ADD_CHILD":
                # Finds the mother Person object
                mother = obj.find_person(shan, command[1])
                # Prints relevant error messages to the console
                if mother is None:
                    print("PERSON_NOT_FOUND")
                elif mother.gender == "Male":
                    print("CHILD_ADDITION_FAILED")
                else:
                    self.family_function_mapping(obj, command[0], mother, command[2], command[3])
                    if populate_family_tree==False:
                        print("CHILD_ADDITION_SUCCEEDED")
            elif command[0] == "ADD_SPOUSE":
                 # Finds the existing spouse Person object
                existing_spouse = obj.find_person(shan, command[1])
                if existing_spouse is None:
                    if populate_family_tree==False:
                        print("SPOUSE_ADDITION_FAILED - PERSON_NOT_FOUND")
                else:
                    self.family_function_mapping(obj, command[0], existing_spouse, command[2], command[3])
            elif command[0] == "GET_RELATIONSHIP":
                person = obj.find_person(shan, command[1])
                if person is None:
                    print("PERSON_NOT_FOUND")
                else:
                    # Most functions need the root of the family tree hence the object 'Shan' is sent
                    output = self.family_function_mapping(obj, command[2], shan, command[1])
                    # If the output is none or no results have been retrieved for the relevant operation
                    if output is None:
                        print("NONE")
                    elif len(output) == 0:
                        print("NONE")
                    else:
                        # Printing all the results in a single line at a time
                        for item in output:
                            print(item.name, end= " ")
                        print()