programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    123: "A piece of code that you can easily call over and over again.",
}

# Printing
# The keyword have to be exactly the same
# Put the right data type for example this one is string so it has to have ""
print(programming_dictionary["Bug"])
print(programming_dictionary[123])

# Adding Value
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Empty Dictionary
empty_dictionary = {}

# Wipe an Existing Dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an Item In A Dictionary
programming_dictionary["Bug"] = "Hello"
print(programming_dictionary["Bug"])
print(programming_dictionary)

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Loop": "A piece of code that you can easily call over and over again.",
}

# Loop Through A Dictionary
# just give the key
for thing in programming_dictionary:
    print(thing)
# give value and key
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])