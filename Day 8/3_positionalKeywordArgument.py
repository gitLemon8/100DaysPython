# Functions with more than 1 input

# Positional Argument
def greet_with(name, year):
    print(f"Hi {name}")
    print(f"You are {year}")

greet_with("Angela", 12)

# Keyword Argument
greet_with(name="Angela", year = 12)