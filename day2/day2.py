# Day 2 Part 1

two = 0

three = 0

with open("boxes.txt", "r") as f:
    for line in f.readlines():
        letters = {}
        for letter in line:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        if 3 in letters.values():
            three += 1
        if 2 in letters.values():
            two += 1

print(two * three)

# Day 2 Part 2

def match(line, code):
    pos = -1

    for i, (char1, char2) in enumerate(zip(line, code)):
        if char1 != char2:
            if pos != -1:
                return -1
            else:
                pos = i

    return pos

with open("boxes.txt", "r") as f:
    codes = set(f.readlines())
    for line in codes:
        for code in codes:
            if match(line, code) is not -1:
                pos = match(line, code)
                print(line[0:pos] + line[pos+1:])
                exit()