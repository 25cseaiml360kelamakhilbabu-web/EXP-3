# Question 5: WAP to print even length words in a string. 
# Answer:Python
def even_length_words(s):
    words = s.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

s = input("enter a string:")
even_length_words(s)
