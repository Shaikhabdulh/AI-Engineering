# Simple Calculator Program
x = float(input("What is x? "))
y = float(input("What is y? "))

print (f"{(x / y):.3f}")
print (f"printing rounded result : - {round(x/y,1):,}")
# This will print the us standerd commas after each thousand or 3 digits format a string :,
# Calculator only works with integer and float only right now.