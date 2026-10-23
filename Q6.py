# Question 6: WAP to remove all duplicates from a given string.   
# Answer:Python
def remove_duplicate(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

s = input("enter a string:")
print("string after removing duplication:", remove_duplicate(s))
