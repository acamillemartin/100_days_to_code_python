# Welcome to the tip calculator!
print("Welcome to the tip calculator!")

# Ask for the total bill
total_bill = float(input("What was the total bill? $"))

# Ask for tip percentage
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))

# Ask for number of people
num_people = int(input("How many people to split the bill? "))

# Calculate the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Calculate total bill with tip
total_with_tip = total_bill + tip_amount

# Calculate amount per person
amount_per_person = total_with_tip / num_people

# Round to 2 decimal places for currency
amount_per_person = round(amount_per_person, 2)

# Print the result
print(f"Each person should pay: ${amount_per_person}")