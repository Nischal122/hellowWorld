menu = '''
1 - Burger           Rs.599
2 - Fries            Rs.299
3 - Soda             Rs.199
4 - Pizza            Rs.100
5 - Salad            Rs.799
Q - QUIT
'''

#print(menu)

user_input = ""
user_order = []

while user_input != "q":
    print(menu)
    user_input = input("what do you like to eat? ").lower()
    food_items = {
        "1": 599,
        "2": 299,
        "3": 199,
        "4": 100,
        "5": 799
    }
    if user_input in food_items:
        a = food_items[user_input]
        user_order.append(a)
        #print(a)
    '''elif user_input not in food_items:
        print("its is out of stock")'''


else:
    total = sum(user_order)
    print(f"Your total is {total} Rs.")
