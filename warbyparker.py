from abc import ABC, abstractmethod


"""
1.	Given a sorted array of numbers(for example [1,4,6,8,9,10]) and a number in the variable i.
Write an efficient search function that looks for i  in the provided array.
In case nothing is found return “False”.

Answer:
I use a simple binary search as the most efficient search function, which has a time complexity of O(logN)
"""
def problem_one_main(sorted_list, i):
    start_point = 0
    end_point = len(sorted_list)-1

    while start_point <= end_point:
        mid_point = (start_point + end_point)//2
        if sorted_list[mid_point] == i:
            return mid_point
        else:
            if i < sorted_list[mid_point]:
                end_point = mid_point-1
            else:
                start_point = mid_point+1

    return False


"""
2.	An airline is looking to do a booking reservation website and is thinking how to prevent a double booking of a 
seat in the case two customers are trying to book the same seat at the same time for a particular flight.  
Write a paragraph or write a pseudo code explaining what database design recommendations would you provide 
to the Airline Company in order to avoid a double booking? (You should mention which SQL statements would you use)

Answer:
I would use a database like SQL Server which has support for transaction locking. Using the With keyword, for example
WITH  ( <table_hint> [ [, ]...n ] )  which would be WITH (TABLOCKX) to obtain an exclusive lock on the table so that
no other users can make changes to the table. An intent lock probably wouldn't be needed since different customers
would only be trying to book for a specific seat at a time, which would probably be represented by a single row of data
whereas intent locks are meant for when locking an entire table is necessary.

A basic pseudo code idea of it would look like this:

BEGIN
UPDATE FLIGHT_SEATS WITH (TABLOCKX) 
SET Seat_taken=name_of_person
WHERE seat_taken=null
"""


"""
3.	A bank asked you to design a class model for their bank accounts. The bank works with two types of accounts, 
Checking and Savings. The savings account can only be created with a minimal deposit of 300 USD while the checking 
doesn’t require an initial deposit. Write the class model creating an abstract class bank account and use the 
concept of inheritance for the Checking and Savings. Also, define a method that only allows creating a saving 
account when there is an initial deposit of 300USD.  

Answer:
In Java, I would use private constructor and a static method that calls the private constructor to limit the user
to only be able to create the Savings account when they input at least 300 for the deposit, the static method
would return a new instance of the savings account object if there is at least 300, otherwise it will return null.

Below is a python implementation
"""
class BankAccount(ABC):
    balance = 0

    def __init__(self, deposit):
        self.balance = deposit

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Cannot reduce balance below $0, please try a different amount")

    # def getBalance(self):
    #     return self.balance

class CheckingAccount(BankAccount):

    def __init__(self, deposit):
        super().__init__(deposit)

class SavingsAccount(BankAccount):
    #I have the constructor raise an ValueError if deposit isn't at least 300
    def __init__(self, deposit):
        if deposit < 300:
            raise ValueError('Deposit insufficient, please deposit at least $300')
        else:
            super().__init__(deposit)

    def withdraw_money(self, amount):
        if self.balance - amount >= 300:
            self.balance -= amount
        else:
            print("Cannot reduce balance below $300, please try a different amount")

"""
4.	Given the following tree, provide a function that search in a recursive way if  the number 3 exists in the tree:
				  1
				 / \
				4   5
               /\    \ 
              8  9    3

Answer:
I am assuming we are working with a tree structure where each parent can only have 2 children. The general idea behind
the search only changes slightly if each node is allowed to have a variable number of children. Some other assumptions
I am making based on this tree example is that there is absolutely no order to the tree, so that left and right
children of a parent node can be greater than or less than the parent, or potentially even equal. Given that it is an
orderless tree, it doesn't really matter if we implement a breadth first search, depth first search, or any other sort
of ordered search of the tree.
"""
class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def recursive_search(node, value):
    if node is None:
        return False
    elif node.value == value:
        return True

    return recursive_search(node.left, value) or recursive_search(node.right, value)


"""
5.	You have $700 in savings for retirement and you deposit 100 dollars every year. 
If your investments earn 10% annually, how much will you have in your retirement account in 8 years? 

Answer:

Year1 = (700 * 1.1) + 100 = 870
Year2 = (Year1 * 1.1) + 100 = 1057
Year3 = (Year2 * 1.1) + 100 = 1262.7
Year4 = (Year3 * 1.1) + 100 = 1488.97
Year5 = (Year4 * 1.1) + 100 = 1737.867
Year6 = (Year5 * 1.1) + 100 = 2011.6537
Year7 = (Year6 * 1.1) + 100 = 2312.81907
Year8 = (Year7 * 1.1) + 100 = 2644.100977

round(problemFiveMain(700, 100, .1, 8), 2) = $2,644.10
"""
def problem_five_main(savings, additional_per_year, interest, years):
    total = savings
    for x in range(0, years):
        total = (total * (1+interest)) + additional_per_year

    return total
"""
6.	Suppose a company has the following revenue and expenses for 2016:
    Revenues of $9,700,000
    Cost of Goods Sold of $1,940,000
    Income Taxes of $2,024,000
    Other Expenses of $500,000 
    Sales, General, & Administrative Expenses of $970,000
          
What’s the net income for the year?

Answer:
Net income is determined by deducting from total revenue all costs, including taxes.

9700000 - 1940000 - 2024000 - 500000 - 970000 = $4,266,000

"""
