print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? "))
tip = int(input("What percent would you like to give? 10, 12, or 15? "))
tip_percent = tip / 100 + 1
people = int(input("How many people will split the bill? "))
pay = (bill / people) * tip_percent
answer = "{:.2f}".format(pay)

print(f"Each person should pay: ${answer}")