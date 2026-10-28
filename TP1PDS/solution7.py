#  Problem 7. Digit Tools 

"""
Without converting numbers to strings, write three functions that work digit by digit with a while loop:
 • digit_sum(n) adds up the digits: 2026 → 2 + 0 + 2 + 6 = 10.
 • reverse_number(n) reverses the digits: 2026 → 6202. 
 • is_palindrome(n) returns True when a number reads the same in both directions (12321). 
(a) Test the three functions with 2026, 12321 and 9875. 
(b) Count how many palindromes there are from 10 to 999. 

"""


def digit_sum(n):
    total = 0
    while n > 0:
        last = n % 10        # last digit
        total = total + last
        n = n // 10          # remove the last digit
    return total


def reverse_number(n):
    reversed_n = 0
    while n > 0:
        last = n % 10
        reversed_n = reversed_n * 10 + last   # add the digit at the end
        n = n // 10
    return reversed_n


def is_palindrome(n):
    return n == reverse_number(n)


# (a) test the three functions
for number in [2026, 12321, 9875]:
    print(f"{number}: digit sum = {digit_sum(number)}, "
          f"reversed = {reverse_number(number)}, "
          f"palindrome = {is_palindrome(number)}")

# (b) count palindromes from 10 to 999
count = 0
for number in range(10, 1000):
    if is_palindrome(number):
        count = count + 1
print("Palindromes from 10 to 999:", count)