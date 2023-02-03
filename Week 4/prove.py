import math

print ("Thanks for eating with us, \please fill in the following information")

child_meal = float( input("Introduce the price of child's meal: "))
adult_meal = float(input("Introduce the price of adult's meal: "))
amount_child = int (input("Introduce the amount of child: "))
amount_adult = int (input("Introduce the amount of adult: "))
tax_rate = float (input("Introduce the tax rate: "))
tip = float (input("would you like to add a tip? Introduce amount: "))

subtotal = (child_meal * amount_child) + (adult_meal * amount_adult )
sales_tax = (subtotal * tax_rate) / 100
total = sales_tax + subtotal + tip

print()
print (f"Subtotal: ${subtotal:.2f}")
print()
print (f"Salex tax: ${sales_tax:.2f}")
print()
print (f"Total: ${total:.2f}")
print()
payment = float(input("Introduce your payment amount: "))

change = payment - total
print()
print(f"change: ${change:.2f}")
print()
print("Come back soon")