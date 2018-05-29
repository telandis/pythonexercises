PLEASE READ EVERYTHING CAREFULLY

PLEASE IMPLEMENT SOLUTIONS IN PYTHON 3 (NOT 2)

Here you will find descriptions of 4 functions with their expected signatures and example inputs and outputs. Please read the assignments for every function very carefully and follow them precisely.

Please provide your solutions in the appropriate portions of solutions.py file that is included alongside this README.

Additionally, please cover all the functions with as many unit tests that you deem necessary. All the unit tests go into tests.py file included alongside this README. 

Your first 2 simple unit tests are written for you as an example. If you run the tests before implementing solutions you should get one failed test. 

You can run your tests like this: python tests.py -v

Please note that by default only test functions that start with `test` like `test_not_four_of_kind` will but run by default. Be careful with your naming. Also, there are many different assert functions in python for unittest library, so please use whichever are most appropriate.

When finished, please zip the `python_tech_screen_junior` folder and send it back vi email.

You will be judged on:
1. Correctness of the solution.
2. Craftsmanship of code.
3. Coverage of code.

Best of luck, and hope to talk to you soon! :)




1. Write a function that takes in a list of numbers and returns a list of all pairs of numbers in that list (not including reverse pairs).
IMPORTANT: please do not use the native function "combinations" or its equivalents

Example 
input: [1, 8, 12, 5, 7] ->
output: [(1, 8), (1, 12), (1, 5), (1, 7), (8, 12), (8, 5), (8, 7), (12, 5), (12, 7), (5, 7)]

def pairs(input):
    """input is a list of ints; output is a list of unique tuple pairs"""


2. Write a function that takes as input a list of five ranks of playing cards and returns a boolean signifying whether the hand contains a four of a kind (four cards of the same rank). Card ranks are represented by STRINGS only.

Example:
is_four_of_kind(["K","Q","K","K","K"]) returns True
is_four_of_kind(["K","Q","3","K","K"]) returns False 

def is_four_of_kind(hand):
    """hand is a list of 5 strings representing card ranks; function is a predicate"""


3. Write the merge part of the merge-sort algorithm. The input lists are already sorted.

Example: 
input: [1, 3, 5], [2, 4, 6]
output: [1, 2, 3, 4, 5, 6]

def merge(a, b):
    """a and b are a list of ints"""


4. Write a function dec_to_base_x that takes 2 arguments:
   1. base - integer from 2 to 9 that represents a base to which a given number should be converted
   2. num - base 10 integer
   And returns a STRING (not an integer) that represents the base 10 number converted to a new base system

Examples:
dec_to_base_x(8, 140) returns "214" 
dec_to_base_x(2, 5) returns "101" 

def dec_to_base_x(base, num):
    """function that converts base 10 number to a number of base from 2 to 9 and returns its STRING representation"""
