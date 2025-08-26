# Switch Consept or MATCH
name=input("Please Enter Your Name :- ")

name=name.title()

match name:
    case "Abdul":
        print("Room Number 60")
    case "Sanjay":
        print("Room Number 20")
    case "Shivam":
        print("Room Number 102")
    case _: # for default case
        print("Who?")
