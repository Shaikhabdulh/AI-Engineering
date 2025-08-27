print("""
Python Collection data types
a collection data type is any data type that can hold multiple
values together in a single variable.
Type    | Ordered?  | Changeable? | Allows Duplicates?       | Example            
--------|-----------|-------------|--------------------------|--------------------
list    | Yes       | Yes         | Yes                      | [1, 2, 3]          
tuple   | Yes       | No          | Yes                      | (1, 2, 3)          
dict    | Yes*      | Yes         | No (keys must be unique) | {"a": 1, "b": 2} where "a" is key and "1" is value  
set     | No        | Yes         | No duplicates            | {1, 2, 3}          
*Note: In Python 3.7+, dict is insertion ordered by default.
""")

# # Dictionary dict = {key:value}: 
# - A built-in data structure used to store data in key-value pairs.
# - Ordered (insertion order is preserved in Python 3.7+).
# - Changeable (mutable).
# - Does NOT allow duplicate keys (but values can be duplicates).
# # Level 1
# students = {
#     "Sanjay":1,
#     "Shyam":2,
#     "Shivam":3,
#     "Sarjil":4
# }
# print (students["Sanjay"])
# print (students["Shyam"])
# print (students["Shivam"])
# print (students["Sarjil"])

# #Level 2 Iterate with for loop
# students = {
#     "Sanjay":1,
#     "Shyam":2,
#     "Shivam":3,
#     "Sarjil":4
# }
# for student in students:
#     print(f"{student} {students[student]}")

# Level 3 make dictionary with 2 values + 1 key = 3 elements.

students = [
    {"name":"Sanjay","Rank":1,"Grade":"A+"},
    {"name":"Shyam","Rank":2,"Grade":"B+"},
    {"name":"Shivam","Rank":3,"Grade":"C"},
    {"name":"Sarjil","Rank":4,"Grade":"D"}
    ]
print(f"name,Rank,Grade") 
for student in students:   
    print(f"{student["name"]},{student["Rank"]},{student["Grade"]}")