# make function
def main():
    i = getinput()
    hallo(i)

def getinput():
    while True:
        n= int(input("What's the Number?\n"))
        if n > 0:
            break
    return n

def hallo(n):
    count=1
    for _ in range(n):
        print (f"{count}) Hallo")
        count+=1

main()