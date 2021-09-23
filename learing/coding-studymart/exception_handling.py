#Error
"""
CompileTime Error - Syntax Error, Namerror
Logical Error - illogical Logic
Runtime Error - running time errror

"""
a = 5
b = 0
try:
    print("Resource Open: ")
    print(a / b)
    n = int(input("please enter a value: "))
except ZeroDivisionError as e:
    print("error")

    print("okay Bye")
except (ValueError, NameError):
    print(ValueError)
except Exception: # all error will be coverd
    print()
finally:

    print("resource close")