'''
Description: This class handles the following important functions:
1. Parsing the input file containing the commands
2. Interpreting the commands and sending it to the relevant functions 
to be implemented
3. Prints the output to the terminal / console
'''

from family_functions import Family_Functions as Fam_Func
from person import Person


class MainClass:
    # Parses the input file    
    def read_input_file(self, input_file):
        f = open(input_file)
        commands = list()
        for line in f:
            commands.append(line.strip("\n").split(" "))
        return commands

    # Interprets the commands in each file
    def call_fam_funcs(self, shan, commands):
        # Object to call methods of Class Family_Functions
        obj = Fam_Func()
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
                    obj.add_child(mother, Person(command[2], command[3]))
                    print("CHILD_ADDITION_SUCCEEDED")
            elif command[0] == "GET_RELATIONSHIP":
                person = obj.find_person(shan, command[1])
                if person is None:
                    print("PERSON_NOT_FOUND")
                else:
                    # Most functions need the root of the family tree hence the object 'Shan' is sent
                    if command[2] == "Paternal-Uncle":
                        output = obj.get_paternal_uncles(shan, command[1])
                    elif command[2] == "Maternal-Uncle":
                        output = obj.get_maternal_uncles(shan, command[1])
                    elif command[2] == "Paternal-Aunt":
                        output = obj.get_paternal_aunts(shan, command[1])
                    elif command[2] == "Maternal-Aunt":
                        output = obj.get_maternal_aunts(shan, command[1])
                    elif command[2] == "Sister-In-Law":
                        output = obj.get_sisters_in_law(shan, command[1])
                    elif command[2] == "Brother-In-Law":
                        output = obj.get_brothers_in_law(shan, command[1])
                    elif command[2] == "Son":
                        output = obj.get_sons(shan, command[1])
                    elif command[2] == "Daughter":
                        output = obj.get_daughters(shan, command[1])
                    elif command[2] == "Siblings":
                        output = obj.get_siblings(shan, command[1])
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