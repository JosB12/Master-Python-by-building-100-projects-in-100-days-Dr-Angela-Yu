import random
import my_module
#
# random_integer = random.randint(1,10)
# print(random_integer)
#
# print(my_module.my_favourite_number)


# random_number = random.random() *11
# print(random_number)

# random_float = random.uniform(0,10)
# print(random_float)

random_coin_flip = random.random() * 11
print(random_coin_flip)
if random_coin_flip <= 3 or random_coin_flip >= 8 and random_coin_flip <= 9 or random_coin_flip == 6:
    print("Heads")
else:
    print("Tails")
