# --- Project 2 ---

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("HHow much tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))


total_bill = tip / 100 * bill + bill
bill_per_person = total_bill / people_count

print(
    f"Each person should pay: {bill_per_person:.2f}"
)  # Or use round(bill_per_person, 2) instead of '.2f'
