price = [10 ,20 ,30]
total = 0
for b in price:
    total += b
    c = total
print("your total is ",c)

for a in range(5):
    for b in range(5):
        print(f"{a} , {b}")

a = [5,2,5,2,2]
for d in a:
    b = ""
    for e in range(d):
        b += "x"
    print(b)



import random

books = ['The Alchemist', 'The Subtle Art of Not Giving a Fuck',
         'It Begins With Us', 'Computer Science Distilled']

random_choice = random.choice(books)

print(random_choice)    # OUTPUT: a random element from the books list