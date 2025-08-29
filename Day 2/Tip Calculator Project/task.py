print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))


# tip_Amount = float(1 + tip / 100)
tip_Amount = float(1+ tip / 100)
tip_amoun_Total = tip_Amount * bill
total_amount = bill * tip_Amount / people

total_amount_rounded = round(total_amount, 2)

print(f"Each person should pay: ${total_amount_rounded}")
