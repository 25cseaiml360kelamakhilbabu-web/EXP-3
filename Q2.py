# Question 2: WAP to find the factorial of a number. 
# Answer:Python
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("enter a number:"))
result = factorial(n)
print("Factorial of", n, "=", result)