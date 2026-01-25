from art import logo

print(logo)

bidders_bid = {}

name = input("Your name: ")
value = int(input("Your bid: "))

bidders_bid[name] = value

isContinue = input("Are there any other bidders? Type 'yes' or 'no'\n\t")
while(isContinue == "yes"):
    print("\n" * 100)
    name = input("Your name: ")
    value = int(input("Your bid: "))

    bidders_bid[name] = value

    isContinue = input("Are there any other bidders? Type 'yes' or 'no'\n\t")

highest_bid = 0
winner = ""

for key in bidders_bid:
    if bidders_bid[key] > highest_bid:
        highest_bid = bidders_bid[key]
        winner = key

print(f"The winner is {winner} with a bid of {highest_bid}")