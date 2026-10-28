#  Problem 8. Flexible Functions: *args, **kwargs and lambda
"""
(a) Write describe(*numbers, decimals=2, label="Data") that accepts any number of values, 
prints their count, min, max and mean (rounded to decimals), 
and returns them as a tuple. With no values it prints "<label>: no values" and returns None. 
(b) Write make_tag(text, **style) that builds an HTML-like string from keyword arguments:
 make_tag("Hello", color="red", size=14) returns <span color="red" size="14">Hello</span>. 
 (c) Write two lambdas: square (returns x²) and is_adult (returns True when age ≥ 18). 

"""

# (a) describe
def describe(*numbers, decimals=2, label="Data"):
    if len(numbers) == 0:
        print(f"{label}: no values")
        return None

    count = len(numbers)
    smallest = min(numbers)
    biggest = max(numbers)
    mean = round(sum(numbers) / count, decimals)

    print(f"{label}: n={count} min={smallest} max={biggest} mean={mean}")
    return (count, smallest, biggest, mean)


# (b) make_tag
def make_tag(text, **style):
    attributes = ""
    for name, value in style.items():
        attributes = attributes + f' {name}="{value}"'
    return f"<span{attributes}>{text}</span>"


# (c) lambdas
square = lambda x: x ** 2
is_adult = lambda age: age >= 18


# Tests
describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()
print(make_tag("Hello", color="red", size=14))
print(square(9), is_adult(17), is_adult(21))