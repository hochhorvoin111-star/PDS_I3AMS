#  Problem 10. Prime Numbers and Goldbach's Conjecture

"""
(a) Write is_prime(n). A prime is a whole number ≥ 2 whose only divisors are 1 and itself. 
For speed, only test divisors d while d * d <= n. 
(b) Print all primes below 50 on one line (use print(..., end=" ")), 
then count the primes below 100. 
(c) Goldbach's conjecture says every even number ≥ 4 is the sum of two primes.
Write goldbach(n) that returns the first pair (p, q) with p + q == n, 
and print the pairs for 4, 6, …, 30. (d) Use a loop with break to check the conjecture 
for every even number from 4 to 10,000.

"""
# (a) prime test
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False      # found a divisor, so not prime
        d = d + 1
    return True


# (b) primes below 50 on one line, then count primes below 100
print("Primes below 50:", end=" ")
for n in range(2, 50):
    if is_prime(n):
        print(n, end=" ")
print()

count = 0
for n in range(2, 100):
    if is_prime(n):
        count = count + 1
print("Number of primes below 100:", count)


# (c) Goldbach pair
def goldbach(n):
    for p in range(2, n):
        q = n - p
        if is_prime(p) and is_prime(q):
            return (p, q)     # first pair found
    return None


for n in range(4, 31, 2):
    p, q = goldbach(n)
    print(f"{n} = {p} + {q}")


# (d) check every even number from 4 to 10000, using break
holds = True
for n in range(4, 10001, 2):
    found = False
    for p in range(2, n):
        if is_prime(p) and is_prime(n - p):
            found = True
            break             # stop searching, we found a pair
    if not found:
        holds = False
        break                 # a counterexample would stop everything
print("Goldbach holds for every even number from 4 to 10000:", holds)