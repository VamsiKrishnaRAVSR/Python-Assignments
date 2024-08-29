def calculate(str):
    try:
        return eval(str)
    except ZeroDivisionError:
        return("Cannot divide with 0")
    except Exception as E:
        return(E)
print(calculate('5+10/0'))
