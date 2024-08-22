import numpy as np 
# # a = np.array([1], dtype="int")
# # print(type(a))

# import array as arr
# p = arr.array('i', [1,23,4])

# p.append(100)
# print(p, len(p))

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(arr)
# print(f"{arr} is === {arr}"+ f"{arr}")
arr = np.delete(arr, 0, axis=1)
a = [10,20,30,40]
# [new_item for item in list if condition]
p = [item for item in a if item > 2]
# print(p)
# p = {1: {
#     1.1: "ANC",
#     1.2: "Pillow"
# }, 2: "Early"}
# x = p.copy()
# x[1] = "AAAA"
# print(x, p)
new_dict = {a[i]: 1 for i in range(len(a))}
# print(new_dict.entries)
q = (1,23,4,0)
# print(q.sorted())

# print(list(filter(lambda x: x%2 ==0 , [1,2,3,4,5,6])))

# try:
#     print(5//0)
# except Exception as E:
#     print(type(E))

def foo():

    try:
        return 1//0
    except Exception:
        return 3
    finally:
        return 2
k = foo()
# print(4+"2")
# import math

# num=int(input("Enter a number of whose factorial you want to find"))

# print(math.factorial(num))

# try:
#     5//1
# except ZeroDivisionError:
#     print("This is wrong")
# else:
#     print("Else executed")

# try:
#     if(4+"E" and 5//0):
#         print("SSS")
# except Exception as E:
#     print(type(E), E.args)
# else:
#     print("LFFF") 

# print(1==int("1"))

# p = open('assignment2.py')
# print(p.readline())

# with open("sample.txt", "w") as p:
#     p.write("abc")
# q = open("sample.txt")
# print(q.read())
# with open("sample.txt", "a") as q:
#     q.write("DEF")

# q = open("sample.txt")
# print(q.read())
# g = (i for i in range(5))

# print(type(g)
# )


# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']

# names2 = names1

# names3 = names1[:]

# names2[0] = 'Alice'

# names3[1] = 'Bob'

# sum = 0

# for ls in (names1, names2, names3):

#     if ls[0] == 'Alice':

#         sum += 1

#     if ls[1] == 'Bob':

#         sum += 10

# print(sum)

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, a, b):
#         # super().__init__()
#         self.a = a
#         self.b =b

#     def area(self):
#         pass

# class Circle(Shape):
#     def area(self):
#         pass
#     pass

# a = Rectangle(10, 15)
# b = Circle()
class demo():

    def __repr__(self):

        return '__repr__ built-in function called'

    def __str__(self):

        return '__str__ built-in function called'

s=demo()

print(s)
"""  """


from MyPackage import calc
help(calc.add_two_numbers)

class Demo:

    def __init__(self):

        self.x = 1

    def change(self):

        self.x = 10

class Demo_derived(Demo):

    def change(self):

        self.x=self.x+1

        return self.x

def main():

    obj = Demo_derived()

    print(obj.change())

 

main()

