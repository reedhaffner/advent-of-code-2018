freq = 0

with open("frequencies.txt", "r") as f:
    for line in f.readlines():
        freq += int(line)

print(freq)
