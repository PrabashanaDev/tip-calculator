name= input("What is your name? ")
print(f"Hello, {name} Welome to RESTURANTNAME")

bill= float(input("What is your total bill? "))
print(f"Your bill is {bill}")

answer= input("Would you like to add a tip?(yes/no) ")
if answer == "yes":
    tip= float(input("How much would you like to tip? "))
    total= bill + tip
    print(f"Your total bill is {total}")
else:
    print(f"Your total bill is {bill}")