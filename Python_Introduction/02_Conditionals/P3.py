# # # Odd Even Finder
# # x = int(input("Please Enter Your Number: - "))
# # if x % 2 == 0:
# #     print ("X is Even")
# # else:
# #     print("X is Odd")

# Now Do it with the function

def main():
    x =int(input("Please Enter your Number: - "))
    if is_even(x):
        print("Even")
    else:
        print ("Odd")

# def is_even(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# def is_even(x):
#     return True if x % 2 == 0 else False #Python option write like you writing in english

def is_even(x):
    return x%2==0
    
main()