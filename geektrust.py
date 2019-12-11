'''
Description: This program is the entry point to the code to solve the following problem:
https://www.geektrust.in/coding-problem/backend/family

It does the following:
1. Read intial family tree commands from Input/Populate_Family_Tree.txt
2. Makes a call to class MainClass to populate the intitial family tree
3. Read the command line argument containing the input commands to the problem
4. Send the input commands to the Main Class that handles parsing the commands
'''
import sys
from person import Person
from main_class import MainClass    

# Constants defined here
MALE = "Male"
FEMALE = "Female"
POPULATE_FAMILY_TREE_FILE = "Inputs/Populate_Family_Tree.txt"

def main():
    # Object of MainClass
    main_class = MainClass()
    # Root of the family tree - King Shan
    shan = Person("Shan", "Male")
    # Constructs the initial family tree based on the problem statement
    # Sends the input populate family tree file for parsing
    commands = main_class.read_input_file(POPULATE_FAMILY_TREE_FILE)
    # Sends the retreived commands to be interpreted 
    # Populate_family_tree = True to suppress print statements while 
    # populating the family tree
    main_class.call_fam_funcs(shan, commands, populate_family_tree=True)
    # Reads the input file absolute path from the command line
    input_file = sys.argv[1]
    # Sends the input file for parsing
    commands = main_class.read_input_file(input_file)
    # Sends the retreived commands to be interpreted
    main_class.call_fam_funcs(shan, commands)


if __name__ == "__main__":
    main()