print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age <= 12:
        print("pay 5 dollars")
    elif age <= 18:
        print("pay $7 dollars")
    else:
        print("pay $12 dollars")
else:
    print("Sorry you have to grow taller before you can ride.")

#BMI Calculator with Interpretations

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
elif bmi >= 25:
    print("overweight")