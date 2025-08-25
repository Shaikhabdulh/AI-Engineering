print("This Program is used to compare two digits")
x=input("Please Enter First value: - ")
y=input("Please Enter Second value: - ")

if x>y:
    print("1st digit is grater then 2nd digit")
    print(f"{x}>{y}")
elif x==y:
    print("1st digit is equal to 2nd digit")
    print(f"{x}={y}")
else:   #elif x<y: no need to check this just else statement can be added
    print("1st digit is lessthen 2nd digit")
    print(f"{x}<{y}")
exit()
#Python require indentation.