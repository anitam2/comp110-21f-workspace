"""Repeating a beat in a loop."""

__author__ = "730408275"


beat: str = input("What beat do you want to repeat? ")
word_repititions: str = input("How many times do you want to repeat it? ")
num_repititions = int(word_repititions)
count: int = 0
word: str = ""

if num_repititions <= 0:
    print("No beat...")
else:
    while count < num_repititions:
        if num_repititions - 1 == count:
            word = word + beat
        else:
            word = word + beat + " "
        count = count + 1
print(word)