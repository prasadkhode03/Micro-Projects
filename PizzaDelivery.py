print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L : ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
if size == "S":
    small_pizza = 15
    if pepperoni == "Y":
        small_pizza = small_pizza + 2
    bill = small_pizza
elif size == "M":
    medium_pizza = 20
    if pepperoni == "Y":
        medium_pizza = medium_pizza + 3
    bill = medium_pizza
elif size == "L":
    large_pizza = 25
    if pepperoni == "Y":
        large_pizza = large_pizza + 3
    bill = large_pizza
else:
    print("Invalid Input!")
if extra_cheese == "Y":
    bill = bill + 1

print(f"Your total bill : {bill}")
    
