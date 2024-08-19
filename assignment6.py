# [“name512”, “same1example”, “joy18full”] replace the digits from string inside list

def replace_digits_with_strings(arr):
    replacedArr=[]
    for word in arr:
        replacedArr.append(''.join(k for k in word if not k.isdigit()))
        
    print(replacedArr)

replace_digits_with_strings(['“name512”', '“same1example”', '“joy18full”'])

# [1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt functions like map, filter or reduce

arr = [1, 'a', 2, 'b', 3, 'c']
digits = list(filter(lambda x: isinstance(x, int), arr))
alphabets = list(filter(lambda x: isinstance(x, str), arr))

print(digits, alphabets)


# [1,2,3,1,3,4,6,5,3] get unique numbers from list with basic constructs

def unique_numbers(arr):
    unique_list = []
    for i in arr:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)

unique_numbers([1,2,3,45, 1, 45, 2, 3])


# Create function to generate data randomly with python standard library
import random

def random_numbers(length):
    arr =[]
    for i in range(length):
        arr.append(random.randint(0, 100))
    return arr
print(random_numbers(10))



# Create function to check if date is in given range

import datetime

def is_date_in_range(date_to_check, start_date, end_date):
    return start_date <= date_to_check <= end_date

today_date = datetime.datetime(2024, 8, 19)
start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 7, 31)

if is_date_in_range(today_date, start_date, end_date):
    print(F"{today_date} is within the range")
else:
    print(F"{today_date} is outside the range")
