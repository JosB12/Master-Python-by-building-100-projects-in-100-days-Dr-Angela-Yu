print('''
            uuuuuuuuuuuuuuuuuuuu
          u" uuuuuuuuuuuuuuuuuu "u
        u" u$$$$$$$$$$$$$$$$$$$$u "u
      u" u$$$$$$$$$$$$$$$$$$$$$$$$u "u
    u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
  u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
$ $$$" ... "$...  ...$" ... "$$$  ... "$$$ $
$ $$$u `"$$$$$$$  $$$  $$$$$  $$  $$$  $$$ $
$ $$$$$$uu "$$$$  $$$  $$$$$  $$  """ u$$$ $
$ $$$""$$$  $$$$  $$$u "$$$" u$$  $$$$$$$$ $
$ $$$$....,$$$$$..$$$$$....,$$$$..$$$$$$$$ $
$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
"u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
  "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
    "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
      "u "$$$$$$$$$$$$$$$$$$$$$$$$" u"
        "u "$$$$$$$$$$$$$$$$$$$$" u"
          "u """""""""""""""""" u"
            """"""""""""""""""""
''')
print("🌴 Welcome to *Treasure Island* 🏴‍☠️")
print("Your mission: find the golden chest before the island swallows it forever.")

first_way = ""
second_choose = ""
third_choose = ""

way = input("👉 You reach a crossroads in the jungle. Do you go left (L) or right (R)? ").lower()
if way == "l":
    first_way = "You push through the dense jungle and arrive at a moonlit crystal lake."
    print(first_way)
    way_two = input("⛵ Do you take the boat (Y) or swim through the dark waters (S)? ").lower()
    if way_two == "y":
        second_choose = "You row the boat across... the water is calm and silent."
        print(second_choose)
        way_three = input(
            "🏰 You reach an ancient fortress with three doors: red (R), blue (B), yellow (Y). Which one do you choose? ").lower()
        if way_three == "y":
            third_choose = "🎉 You push open the yellow door and discover the hidden treasure. YOU WIN!"
            print(third_choose)
        else:
            third_choose = "💀 Behind the door lies a deadly trap. The treasure is lost forever. GAME OVER."
            print(third_choose)
    else:
        second_choose = "You dive in, but hungry sharks surround you. 🦈 GAME OVER."
        print(second_choose)
else:
    first_way = "⚔️ Pirates ambush you on the right path and capture you. GAME OVER."
    print(first_way)
