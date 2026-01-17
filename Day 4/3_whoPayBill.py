import random
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

rand_num = random.randint(0, 4)
print(friends[rand_num])

# Alternative solutions
print(random.choice(friends))