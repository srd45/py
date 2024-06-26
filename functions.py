def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return int(num1)+int(num2)

total = sum(7,2)
print(total) 