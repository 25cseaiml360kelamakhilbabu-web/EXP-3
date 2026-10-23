# Question 4: WAP to check whether the string is symmetrical or palindrome.
# Answer:Python
def check_string(s):
    if s == s[::-1]:
        print("The string is palindrom")
    else:
        print("The string is not palindrom")

    n = len(s)
    if (n % 2 == 0):
        mid = n // 2
        if s[:mid] == s[mid:]:
            print("The string is symetrical")
        else:
            print("The string is not symetrical")

S = input("enter a string:")
check_string(S)