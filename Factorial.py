n = int(input("num>: "))
factorial = 1
while n != 0:
    for i in range(1, n+1):
        factorial *= i
    print(factorial)
    break
else:
    print(f"it's a '{n}' ")
