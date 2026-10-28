# Problem 4: Type-Conversion Detective

# Part A:  Copy the table into your notebook. Predict the result of each expression first, then check it in Python. 


print(int("7") + 3.5)
print(str(10) * 3)
print(bool(""), bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10 / 2))


"""
Expression                  Your prediction                 Python's answer
int("7") + 3.5              10.5                            10.5
str(10) * 3                 101010                          101010
bool(""), bool(" ")         False True                      False True
int(3.99)                   3                               3
float("1e3")                1000.0                          1000.0
int(True) + float("2.5")    3.5                             3.5
round(2.5), round(3.5)      2 4                             2 4
type(10 / 2)                <class 'float'>                 <class 'float'>

"""

# Part B: Write a function safe_int(text) that turns a string into an int. It must accept spaces around the number, negative numbers and decimals ("3.9" → 3), and return None when the text is not a number. 

def safe_int(text):
    text = text.strip()
    try:
        number = float(text)
        return int(number)
    except ValueError:
        return None

for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))