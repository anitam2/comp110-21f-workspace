"""Finding duplicate letters in a word."""

__author__ = "730408275"

word = input("Enter a word: ")
duplicate: bool = False

i: int = 0
while i < len(word): 
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            duplicate = True
        j += 1 
    i += 1
    
print("Found duplicate: " + str(duplicate))