print("""
Python Collection data types
a collection data type is any data type that can hold multiple
values together in a single variable.
Type    | Ordered?  | Changeable? | Allows Duplicates?       | Example            
--------|-----------|-------------|--------------------------|--------------------
list    | Yes       | Yes         | Yes                      | [1, 2, 3]          
tuple   | Yes       | No          | Yes                      | (1, 2, 3)          
dict    | Yes*      | Yes         | No (keys must be unique) | {"a": 1, "b": 2}   
set     | No        | Yes         | No duplicates            | {1, 2, 3}          
*Note: In Python 3.7+, dict is insertion ordered by default.
""")

# List : - list is a built-in data structure used to store a collection of items.
# Lists are ordered[Follow Sequence start from 0 to ...]
# Changeable (mutable)
# Contain duplicates.
# Level 1
# students=["Sanjay","Shyam","Shivam","Sarjil"] # my list having 4 elements.

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])

# Level 2
# # How to iterate loop with for loop.
# students = ["Sanjay","Shyam","Shivam","Sarjil"]
# counter=0
# for student in students:
#     counter+=1
#     print (f"{counter}) {student}")

# Can you create function of it's logic
# lets do that
def main():
    students = ["Sanjay","Shyam","Shivam","Sarjil"]
    lookup(students)

# def lookup(l1):
#     size=len(l1)
#     print("Total List Size is : - ",size) # Total Size of List
#     counter=1
#     for data in l1:
#         if counter == 2:
#             counter+=1
#             continue
#         print(f"{counter}) {data}")
#         counter+=1
# insted do this with the help of enumerate built in function.

def lookup(l1):
    size = len(l1)
    for index, data in enumerate(l1, start=1): # Return an enumerate object start from 1 and store the sequence into index and data into data variable mainly return [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')] tuple type data
        print(f"{index}) {data}") 
main()