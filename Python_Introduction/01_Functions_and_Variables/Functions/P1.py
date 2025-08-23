print("""
print ("Hello Wolrd")
"print" is build in function
"Hello World" is argument 
if you run this file the "output" will be the *SIDE EFFECT* or outcome of this function.
""")
name=input("Please Insert your name : - ")
# print("hello, "+name) # + operator Allow you to Connect two strings means concatination.
print ("hello, MR. ", end=" ") # end peremeter allow you change default behaviour.

# # Remove whitespaces from str
# name=name.strip()

# # Capitalize user's name first word only
# name=name.capitalize()

# # Capitalize each word 
# name=name.title()


# What is Parameter are just place holder and argument are value passed by the user or developer.and
#There are two type of argument 1 named 2 positional arguments
#named argument are not bound to the sequence and positional arguments are bound with the sequence.

#user defined function
# this function allow you to remove white spacess and capitalize each word of your string.abs
def captal(x):
    x=x.strip() # remove white space
    x=x.title() # make all words capital
    z=x.split()
    z=len(z)
    if z==2:
        return x    # Return value will be printed if the first and last name is filled
    else:
        print ("\nPlease enter proper value full Like this")
        print ("\nEXAMPLE : - FIRSTNAME LASTNAME")
        print ("\n                JOHN WIKE")
        exit()

name=captal(name) # store that value into name variable again
first, last = name.split(" ") # Split words by space

print (last)
# no i have one more prolbem where i want to split user name and call him by her last name()