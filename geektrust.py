'''
Description: This program is the entry point to the code to solve the following problem:
https://www.geektrust.in/coding-problem/backend/family

It does the following:
1. Make a call to class Populate_Family to populate the intitial family tree
2. Read the command line argument containing the input commands to the problem
3. Send the input commands to the Main Class that handles parsing the commands
'''
import sys
from person import Person
from populate_family import Populate_Family as Pop_Fam
from main_class import MainClass    


def main():
    # Object of MainClass
    main_class = MainClass()
    # Root of the family tree - King Shan
    shan = Person("Shan", "Male")
    # Object of Populate_Family
    pf = Pop_Fam()
    # Constructs the initial family tree based on the problem statement
    pf.populate_family(shan)
    # Reads the input file absolute path from the command line
    input_file = sys.argv[1]
    # Sends the input file for parsing
    commands = main_class.read_input_file(input_file)
    # Sends the retreived commands to be interpreted
    main_class.call_fam_funcs(shan, commands)


if __name__ == "__main__":
    main()