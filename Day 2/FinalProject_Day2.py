print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip_percentage = float(tip/100) * float(total_bill)
bill_plus_tip = total_bill + tip_percentage
bill_per_person = round(bill_plus_tip / number_of_people, 2)

print(f"Each person should pay: ${bill_per_person}")