print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

# todo: work out how much to add to their bill based on their pepperoni choice
if pepperoni == 'Y' and size == 'S':
    bill += 2
elif pepperoni == 'Y' and (size == 'M' or size == 'L'):
    bill += 3

# todo: work out their final amount based on whether if they want extra cheese
if extra_cheese == 'Y':
    bill += 1
else:
    bill += 0

# final bill
print(f"Your final bill is: ${bill}")