print("Welcome to Python Pizza Deliveries!")
pizza_price = 0
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price = 20
elif size == "L":
    pizza_price = 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    else:
        pizza_price += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    pizza_price += 1
print(f"Your final bill is: ${pizza_price}.")


