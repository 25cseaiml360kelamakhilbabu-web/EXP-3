# Question 1: WAP to print twin prime numbers between 1 to N.  
# Answer:Python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("enter the value of n:"))
print("twin prime numbers between 1 and", n, "are:")
for i in range(2, n - 1):
    if is_prime(i) and is_prime(i + 2) and (i + 2) <= n:
        print(f"({i}; {i+2})")

