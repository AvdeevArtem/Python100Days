total_bill = float(input("What was the total bill? $"))
tips = int(input("How much tip would you like to give? 10, 12 or 15 "))
total_persons = int(input("How many people to split the bill "))
total_bill_with_tips = total_bill + (total_bill * tips / 100)
print(f"Each person should pay ${round(total_bill_with_tips / total_persons,2)}")

