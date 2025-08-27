# make loop of printing patterns.
# # Level 1 Print column
# def main():
#     c=int(input("how many column you want: - "))
#     print_column(c)

# def print_column(height):
#     for _ in range(height):
#         print("#")
# main()

# # Level 2 Print Row
# def main ():
#     r=int(input("how many Row you want: - "))
#     print_row(r)

# def print_row(width):
#     for _ in range(width):
#         print("?",end="")
#     print("")

# main()

# Level 3 Create simple 3 by 3 square
def main():
    ui=int(input("how many square you want: -"))
    print_square(ui)

def print_square(size):
    # For loop for Printing Row
    for r in range(size):
    # For loop for Printing Column
        for c in range(size):
            # Print single brick
            print("#",end="")
        # Add Line after each Row
        print()
        
main()