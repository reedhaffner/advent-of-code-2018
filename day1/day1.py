# Day 1 Part 1

freq = 0

with open("frequencies.txt", "r") as f:
    for line in f.readlines():
        freq += int(line)

print(freq)

# Day 1 Part 2

freq = 0

freqs = set()

while True:

    with open("frequencies.txt", "r") as f:
        for line in f.readlines():
            freq += int(line)
            if freq in freqs:
                print(freq)
                quit()
            freqs.add(freq)