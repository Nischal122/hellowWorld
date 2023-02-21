a = float(input("write first number "))
b = float(input("write second number "))
c= str(input("what do u want to do;add(+),subtract(-),multiply(*),divide(/) "))

if c == "+":
    add = (a+b)
    print("Sum between two numbers are;",round(add, 3))
elif c == "-":
    add = (a-b)
    print("difference between two numbers are;",round(add, 3))
elif c == "*":
    add = (a*b)
    print("multiplication between two numbers are;", round(add, 3))
elif c == "/":
    add = (a/b)
    print("division between two numbers are;", round(add, 3))
else:
    print("get lost :( its a error")