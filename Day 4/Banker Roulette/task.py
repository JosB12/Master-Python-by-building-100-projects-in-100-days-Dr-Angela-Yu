import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# option 1
# random_friend = random.choice(friends)
# print(f"{random_friend} is going to buy the meal today!")

# option 2
print(random.choice(friends))

#option 3
random_index = random.randint(0, len(friends)-1)
print(friends[random_index])