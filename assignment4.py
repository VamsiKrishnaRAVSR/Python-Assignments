import time
import random
# Convert the list [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10] with list comprehension
given_list = [1, 2, 3, 4, 5]
p = [x*2 for x in given_list]
print(p)

# Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec
def retry():
    def decorator(func):
        def wrapper(*args, **kwargs):
            retires = 0
            while retires < 3:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    time.sleep(3)
                    if(retires < 3):
                        retires+=1
                        print(F"{retires} retry failed.Reason - {e}")
            else:
                return Exception("Max retires crossed")

        return wrapper
    return decorator

@retry()
def example_function():
    # Need to create failed and pass scenario, Loops doesnt work here. 
    if random.choice([True, False]):
        raise Exception("Random failure occurred!")
    return "Success!"

# Call the function
result = example_function()
print(result)


# Build a counter generator. SINCE NO DESCRIPTION IS PROVIDED, I ASSUMED BELOW AS QUESTION
# This is a finite counter, Where we take user input till where i need to run this. 

def counter(max_value):
    num = 0
    while num <= max_value:
        yield num
        num += 1

max_count = int(input("Enter the maximum value: "))
# THIS FOR LOOP INTERNALLY CALLS THE NEXT() FUNCTION SO THAT THIS FUNCTION KEEPS ON EXECUTING TILL 
for number in counter(max_count):
    print(number)
