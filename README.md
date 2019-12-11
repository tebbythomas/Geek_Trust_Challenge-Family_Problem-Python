# Geektrust Family Problem - Python Solution - <a href="https://www.geektrust.in/coding-problem/backend/family">Problem Definition Link</a>

<p>
This repository contains the classes, test cases and inputs related to Geektrust's Family problem.
<br />
<b>Run the code using the following command:</b>
```
python geektrust.py <Absolute-Path-To-Input-File>
```
Eg:
```
python geektrust.py <Absolute-Path-To-Input-File>/Inputs/Input1.txt
```
<b>Run the tests using the following command:</b>
<br />
```
python test_geektrust_family.py
```
The code contains the following files:
<br />
<br />
<b>1. geektrust.py: </b> Entry to the code. Initial family tree is populated, calls to parse input file and interpret commands
<br />
<b>2. main_class.py: </b> Input file is parsed, input commands interpreted, calls sent to family functions, output sent to the terminal
<br />
<b>3. person.py: </b> contains the relevant attributes of a person
<br />
<b>4. populate_family.py: </b> used to contruct the family tree according 
to the problem definition. 
<br />
The root is created first - King Shan. All subsequenet family members are added via two operations: Add child, Add spouse
<br />
<b>5. test_geektrust_family.py: </b> contains the test cases to test all the family functions defined
<br />
<b>6. Inputs folder - </b>Contains 6 sample inputs that can be used to test the code
<br />
<b>7. Outputs folder - </b>Contains the expected outputs corresponding to the 6 input files
</p>