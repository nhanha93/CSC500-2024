print("Total of your meal")
price = float(input("Please enter the price of your meal: "))
tax = 0.7 * price
tip = 0.18 * price
with_tip = price + tip
with_tax = price + tax
total = price + tax + tip
print("Tax amount is $ ", tax)
print("Tip amount is $ ", tip)
print("Your total is $", total)