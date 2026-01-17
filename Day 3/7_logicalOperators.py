height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    # Logical Operator used here:
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        bill = 12
    
    # ... rest of the photo and bill code