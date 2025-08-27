# In this topic, we will focus on errors — the things that prevent our program from running properly.
# An error is a problem that stops your code from executing.
# There are mainly two types of errors:

# 1) Syntax Error:
#    - Occurs when you write code that doesn't follow Python's rules or structure.
#    - Example: missing colon, wrong indentation, unmatched parentheses, etc.
# Run & Check
# print("Hello world)
#  SyntaxError: unterminated string literal (detected at line 13)


# 2) Runtime Error (Exception):
#    - Occurs when the code is syntactically correct but causes an error while running.
#    - Example: dividing by zero, using a variable that hasn’t been defined(Accept outside of for loop), etc.
# Run & Check
# i=int(input("checking your input: - "))
# print(f"i is {i}")
# ValueError: invalid literal for int() with base 10: 'a' trying to enter str in place holder int.

#Now we handle exception
#We are just right now handling run time error
# # Level 1 Try except errors
# try:
#     i=int(input("checking your input: - "))
#     print(f"i is {i}")
# except ValueError:
#     print("X is not an intigers") # This allows for to entry appropriate error.

# # Level 2 Make sure the try block is as minimal as possible.
# def main():
#     x=get_int()
#     print(f"x is {x}")

# def get_int():
#     while True: # Infinit loop
#         x=input("What is your input : - ")
#         try:
#             if x == 'exit': # if input having typed exit in string it will put break
#                 exit()
#             int(x) # try to convert x(string) into integer
#         except ValueError:
#             print("x is not an integer or Please type exit -> exit")
#         else:
#         #     print(f"x is {x}")
#         #     print("Please type exit -> exit")
#                 return x

# main()


# # Level 3 more compact and clean version
# def main():
#     x=get_int()
#     print(f"x is {x}")

# def get_int():
#     while True: # Infinit loop
#         x=input("What is your input : - ")
#         if x.lower() == 'exit': # if input having typed exit in string it will put break
#             exit()
#         try:
#             return int(x)
#         except ValueError:
#             print("x is not an integer or Please type exit -> exit")  
# main()

# Level 1 Pass the error and ignore the error
def main():
    x=get_int("What is x: - ")
    print(f"x is {x}")

def get_int(prompt):
    counter=1
    while True: # Infinit loop
        x=input(prompt)
        if x.lower() == 'exit': # if input having typed exit in string it will put break
            exit()
        try:
            return int(x)
        except ValueError:
            #pass # also added to pass or continue without giving error
            counter+=1
            if counter>3:
                counter=1
                print("Please press exit to exit the program")
main()

# take avay : - try,except,pass,raise (create your own error)
# try allow you to check condition
# except try to handle exception
# except pass allow you to just pass
# raise raise your own exception error