# # Understanding Loops 
# # While
# Level 1 While Loop
# i=int(input("Number : - "))
# while i != 0:
#     print (f"{i}) Helo")
#     i = i - 1

# Level 2 While Loop
# i=int(input("Please Insert Number : - "))
# i=i+1 # Juggad
# n=1

# while n<i:
#     print(f"{n}) Hallooo!")
#     #n=n+1
#     n+=1

# For
# Level 1 For loop
# loop iterates over each element in the list
# for i in [0,2]:  # in our case our list have 2 elements.
#     print("Hallo")
# Method 2
# i = int(input("Insert Number : - "))
# n = 1
# for _ in range(i):  # Use _ if you’re not going to use the loop variable — it signals “I’m not going to use this variable.”
#     print(f"{n}) Hallo")  # range(3) is a built-in Python function that generates a sequence of numbers starting from 0 up to but not including 3.
#     n+=1
# Method 3
# print(f"Hallo\n" * 3, end="")

# # Level 2 Combining While and for loop.
# while True:
#     n = int(input("Enter Your Number : - "))
#     if n > 0:
#         break
# for _ in range (n):
#     print(f"{_}) Hallo")
# _+=1 # Juggad
# print(f"{_} Hallo")