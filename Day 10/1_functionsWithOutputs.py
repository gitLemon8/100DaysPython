# def format_name(f_name, l_name):
#     # .title()
#     print(f_name.title())
#     print(l_name.title())

# format_name(f_name="angela", l_name="ANGELA")

# # With f string
# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     print(f"{formatted_f_name} {formatted_l_name}")

# format_name("AnGeLa", "YU")

# With return statement
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("AnGeLa", "YU")
print(formatted_string)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_1("hello")
print(output)

# Take output of function_1 and insert to function_2
output = function_2(function_1("hello"))
print(output)