# Create arithmetics class to calculate avg, mean, mode and standard deviation
import math
class Arithmetic:
    def __init__(self, arr):
        self.arr = arr
    
    def mean(self):
        if(len(self.arr)>0):
            return sum(self.arr)/len(self.arr)
        else:
            return 0
    
    def mode(self):
        data={}
        if(len(self.arr)>0):
            for num in self.arr:
                if num not in data:
                    data[num] = 1
                else:
                    data[num]+=1
            max_value = max(data.values())
            modes = [key for key, val in data.items() if max_value == val]
            # for key, val in data.items():
            #     if(max_value == val):
            #         modes.push(key)
            if(len(modes) >1 ):
                return sum(modes)/len(modes)
            else:
                return modes
        else:
            return 0
        
    def median(self):
        sorted_arr = sorted(self.arr)
        n = len(sorted_arr)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
        else:
            return sorted_arr[mid]

values=[1,2,3,4,5, 1]
arithmetic = Arithmetic(values)
print(arithmetic.mode())
print(arithmetic.mean())
print(arithmetic.median())


# Create a program to validate the age of the voter with the help of custom exception. 
# Voters whose age is less than 18 should not be allowed to vote.


class NotEligibleToVote(Exception):
    def __init__(self, message="Age must be greater than 18"):
        self.message = message
        super().__init__(self.message)

age = int(input("Enter age:"))
if(age<18):
    raise NotEligibleToVote()
else:
    print("you're eligible to vote")


# Create a program to check eligibility of the person for loan  with the help of oops concepts and exception handling.
# Person whose salary is less than 10K/ Month will not be eligible for the loan.

class NotEligibleForLoan(Exception):
    def __init__(self):
        self.message = "Sorry, you're not eligible for loan"
        super().__init__(self.message)

class Person:
    def __init__(self, name, salary, loan_amount):
        self.name = name
        self.salary = salary
        self.loan = loan_amount

    def check_loan_eligibility(self):
        if(self.salary >10000):
            return "You're elligible for the loan"
        else:
            raise NotEligibleForLoan

name = input("Enter your name:")
salary = float(input("Enter your salary in rupees:"))
loan_amount = float(input("Enter loan amount needed:"))

customer1 = Person(name, salary, loan_amount)
customer1.check_loan_eligibility()
