print("Welcome to the tip calculator!")

bill = float(input("Waht was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill?"))

total = bill*((100+tip)/100)

p_total = round(total/people,2)

print(f"Each person should pay: ${p_total}")