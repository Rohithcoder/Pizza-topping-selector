#This program show the toppings and helps them choose the toppings
print("Welcome to PIZZA HUT")
list1 = []
No_toppings = (int(input("How many toppings would you like on your pizza: ")))
if No_toppings == 0:
    print("No toppings were added to you pizza")
else:
    toppings_list = ["Pepperoni", "Cheese", "Tomatoes", "Brocoli", "Bacon"]
    print("These are the toppings")
    for items in toppings_list:
        print(items)
    for l in range(1, No_toppings+1):
        order = str(input("Enter the toppings you want: "))
       
        list1.append(order)
    print(list1)
list1 = []