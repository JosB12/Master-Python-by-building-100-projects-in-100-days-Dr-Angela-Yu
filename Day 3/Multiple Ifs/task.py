print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age <= 12:
        bill = 5
        print("child tickets are 5 dollars")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7 dollars")
    else:
        bill = 12
        print("Adult tickets are $12 dollars")

    want_photo = input("Would you like to have a photo take ? type y for Yes or n fot Not")
    if want_photo == "y":
        bill += 3
    print(f"Your ticket cost is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

