num = int(input("write a number: "))

print("The prime numbers up to", num, "are:")

for i in range(2, num+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
