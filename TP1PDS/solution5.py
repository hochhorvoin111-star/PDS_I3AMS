#  Problem 5. Letter Grade

"""
Write a function letter_grade(score) that returns a letter according to this scale. Any score below 0 or above 100 must return "Invalid". 
(a) Test your function with the list [99, 90, 85.5, 72, 60, 59.9, -5, 101] and print the results aligned as below.
(b) Why must the test for A+ come before the test for A? What happens if you swap them? 

"""

def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for score in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
    print(f"{score:>5} -> {letter_grade(score)}")
        
