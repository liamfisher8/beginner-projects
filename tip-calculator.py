print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
percent = input("What percentage tip would you like to give 10, 12 or 15?")
people = input("How many people split the bill?")

no_tip = float(bill) / float(people)
with_tip = round(no_tip * (1+ (float(percent)/ 100)), 2)



print(f"Each person should pay: ${with_tip}")
