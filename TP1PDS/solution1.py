# Problem 1. Student Profile Card

""""
Create five variables that describe a student: name (str), age (int), major (str), gpa (float) 
and is_scholar (bool). 
(a) Print a profile card exactly like the one below. The GPA must always 
show 2 decimals (hint: f"{gpa:.2f}"). 
(b) Below the card, print every value followed by the name of its type, 
using type(value).__name__. 
(c) Re-assign age = "20" and print type(age) again. What does this tell you about dynamic typing? 

"""

# Create five variables that describe a student:

name = "Sok Dara"
age = 20
major = "Data Science"
gpa = 3.8
is_scholar = True

print("=================================")
print(f"Name           :{name}")
print(f"Age            : {age}")
print(f"Major          : {major}")
print(f"GPA            : {gpa:.2f}")
print(f"Scholar        : {is_scholar}")
print("=================================")

print(name, type(name))
print(age, type(age))
print(major, type(major))
print(is_scholar, type(is_scholar))