# Temperature Converter 

"""
rite two functions: celsius_to_fahrenheit(c, round_to=1) and 
fahrenheit_to_celsius(f, round_to=1). Use the formula F = C × 9/5 + 32 
and return the result rounded with round(value, round_to). 
(a) Use a for loop with range(0, 101, 20) to print the conversion table below. 
(b) Convert 98.6 °F (normal body temperature) to Celsius. 
(c) Convert 37 °C to Fahrenheit and back again. Do you get 37.0? 
(d) Call one function with round_to=3. Why is a default argument useful here? 

"""

def celsius_to_fahrenheit(c, round_to=1):
    f = c * 9 / 5 + 32
    return f

def fahrenheit_to_celsius(f, round_to=1):
    c = (f - 32) * 5 / 9
    return c
print("s °C |     °F")
print("-----+----------")
for c in range(0, 101, 20):
    print(f"{c:4} | {celsius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")