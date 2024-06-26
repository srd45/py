class JustNOtCoolError(Exception):
    pass

x = 2
try:
    raise JustNOtCoolError("This isn't cool, man.")
    #raise Exception("I'm a custom exception")
    #print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("Name error mean something is probably not defined.")
except ZeroDivisionError:
    print("Please do not divide by 0")
except Exception as error:
    print(error)

else:
    print("No errors!")

finally:
    print("I'm going to print with or without an error.")