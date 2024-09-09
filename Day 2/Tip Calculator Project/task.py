print("Welcome to the Tip Calculator!")
bill_amount = float(input("What was the total bill?"))
tip_percentage = int(input("How much tip would you like to give? 10 12 15?"))
number_of_people = int(input("How many people to split the bill?"))

tip_percentage_to_decimal = tip_percentage / 100 + 1
total_bill = bill_amount * tip_percentage_to_decimal
individual_amount_due = round(total_bill / number_of_people, 2)
print(f"Each person should pay: ${individual_amount_due}")