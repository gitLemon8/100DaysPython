# https://docs.python.org/3/tutorial/datastructures.html
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]

# Accessing Lists start from index 0, - from last
print(states_of_america[-2])
print(states_of_america[0])

# Changing Data Inside List
print(states_of_america[1])
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# Append New Country
states_of_america.append("Angelaland")
states_of_america.extend(["Jack Bauer Land", "Meiland"])
print(states_of_america)

