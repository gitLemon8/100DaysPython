# https://docs.python.org/3/library/random.html
import random

random_integer = random.randint(1, 10)
print(random_integer)

#semi-random exclusive of 1
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

random_number = random.randint(0,1)
if random_number == 0:
    print("Heads")
elif random_number == 1:
    print("Tails")