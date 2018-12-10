from string import *

# day 5 part 1
def destroy(string):
    newlines = [""]
    for letter in string:
        lastletter = newlines[-1]
        if not lastletter == letter and lastletter.lower() == letter.lower():
            newlines.pop()
        else:
            newlines.append(letter)
    return len(newlines) - 1


polymer = open('polymer.txt').read().strip()
print(destroy(polymer))
# day 5 part 2
print(min(destroy(char for char in polymer if char.lower() != letter) for letter in ascii_lowercase))


"""
MY SOLUTION WAS INEFFICIENT (took around 10 minutes), THIS IS FROM u/andreyrmg, WRITTEN WITH WORD VARIABLES TO HELP MY UNDERSTANDING
"""