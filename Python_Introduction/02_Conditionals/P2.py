print("This program is used to give you grade")
grade=int(input("Please Enter Your Grade: -"))

if grade>=101: # prevent user from entering irrelevent worlds and above 100 value
    print("The Grade cannont be above 100")
elif grade>=90:
    print("Grade A;")
elif grade>=80:
    print("Grade B;")
elif grade>=70:
    print("Grade C;")
elif grade>=60:
    print("Grade D;")
else:
    print("Grade F;")