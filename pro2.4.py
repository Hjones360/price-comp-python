#!/usr/bin/env python3

# display a welcome message
print("Price Comparison")
print()

# get input from the user
price_64= float(input("Price of 64 oz size: "))
price_32 = float(input("Price of 32 oz size: "))

# calculate Price per ounce
per_Oz_64 = round(price_64 / 64, 2)
per_Oz_32 = round(price_32 / 32, 2)

# format and display the result
print()
print("Price per oz (64 oz): " + str(per_Oz_64))
print("Price per oz (32 oz): " + str(per_Oz_32))



