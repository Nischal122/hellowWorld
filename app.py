#a calculator that can do + - * /
a=float(input("write first number "))
b=float(input("write second number "))
c= str(input("what do u want to do;add(+),subract(-),multiply(*),devide(/) "))

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
    print("divisition between two numbers are;", round(add, 3))
else:
    print("get lost :( its a error")


#change kg into pound

a=float(input("what is your weight "))
b=input("is it in (k)g or (L)bs ")

if b =="k" or b== "K":
    c= round(a*2.20462 , 3)
    print("Your weight in pound is; ", c)
elif b =="L" or b=="l":
    d= round(a/2.20462 ,)
    print("your weight in kg is;" , d)
else:
    print("cleck your input its error:(")

y=input("write a num ")
x=1
while x<=int(y):
    print(x)
    x=x+1

print("the num u inter ",str(y))

z = input("Again? (Y)es or (N)o ")

if z== "y" or z== "Y" :
    print("ok")

elif z=="n" or z=="N":
    print("so bad")

#the new one
print('price of the house is 1M')
credit=input("do you have good cr, (Y)es/(N)o ")
if credit == "y" or credit == "Y":
    print("you need to pay 10 % down")
    a=1000000/100*10
    print("i.e " , a)

else:
    print("you need to pay 20 % down")
    b = 1000000 / 100 * 20
    print('i.e ', b)

#CLZ WORK TO FIND % AND ALL xd

a=float(input("what's your marks on math? "))

b=float(input("what's your marks on math? "))

c=float(input("what's your marks on math? "))

d=float(input("what's your marks on math? "))

e=float(input("what's your marks on math? "))

f=float(input("what's your marks on math? "))

User_Input = input('''

What are you looking for 
1 - To find percent " % "
2 - To find average ?
3 - To find to total sum of all Marks ?
4 - To find the GPA?
''')

# no; 3 to find the sum of all
if User_Input == "3":
    print("The sum of given marks is; " , a+b+c+d+e+f)

# no; 1 to find the %
elif User_Input == "1":
    print("Taking full marks of all subject is equal to 100 ")
    sum = a+b+c+d+e+f
    percent =round(sum/600*100, 3)
    print(f'''
    Thus your total % is; {percent}
    ''')

# no; 2 to find the average
elif User_Input == "2":
    sum= a + b + c + d + e + f
    average = sum / 6
    print(f'''
    The average of given marks is; {average}
    ''')

#to find the GPA of given marks
elif User_Input == "4":
    sum = a + b + c + d + e + f
    percent = sum / 600 * 100
    Round = percent / 25
    GPA = round(Round , 3)
    print(f'''
    Your obtain GPA is {GPA}
    ''')

else:
    print("Check your input its wrong! select the number from 1 - 4 ")

# count char/letter of word and print name must be 20 char;

name = input("what is your name? ")

if len(name)<3:
    print("name must be more than 3 char")
elif len(name)<=20 :
    print(f"name looks good; {name}")

else:
    print("name must be max 20 char")

#guess the number game

print("guess the number within 3 chance; ")
correct_num = 8
total_guess = 0
while total_guess<3:
    total_guess=total_guess+1

    your_guess=int(input('guess= '))
    if your_guess == correct_num:
        print("you won")
        break
else:
    print(f"you lost the correct num is {correct_num}")


# The car game

print("Type\/\n In-To start car\n Out- to exit \n stop- To stop car\n Help- To get help\n")
key = ""
started = False  # not_started
while True:  # key != "out":
    key = input("keep your key 'IN' or 'out'? ").lower()
    if key == "in":
        if started:
            print("your car is already started")
        else:
            started=True
            print("your car has been started")
        # print("your Car is started.")
    elif key == "help":
        print('>There is no help for you STF and do your thing by your own XD')
    elif key == "stop":
       if not started:
           print("your car is already stopped")
       else:
            started=False
            print("your car is stopped")
    elif key == "out":
        break
    else:
        print("what is this umm ")




# Finding the average and all math thing XD

#gpa totalmarks avg percentage
subjects = []
for x in range(5):
    number = int(input("Enter Your marks for subject"))
    subjects.append(number)
print(subjects)
task = input("Enter your task\n:1>total marks\n2>percantage\n3>gpa\n")
total = 0
for x in range(5):
    total+=subjects[x]
percanatge = total/500 * 100
if (task=="1"):
    print(total)
elif(task=='2'):
    print(percanatge)
elif(task=='3'):
    print(percanatge/25)
else:
    print(total//5)

# ajajabda
a = [5,2,5,2,2]
for d in a:
    b = ""
    for e in range(d):
        b += "x"
    print(b)

#jg csf
price = [10,20,30]
total = 0
for b in price:
    total += b
    c = total
print("your total is " , c)

for a in range(5):
    for b in range(5):
        print(f"{a} , {b}")

