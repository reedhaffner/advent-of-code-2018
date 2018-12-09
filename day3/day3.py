import re

# day 3 part 1
claims = set()
overlaps = set()
sqin = 0

with open("claims.txt", "r") as f:
    print("Working...")
    for line in f.readlines():
        reger = re.compile("#(\d+) @ ((\d+),(\d+)): ((\d+)x(\d+))")
        reg = reger.search(line)
        claim_num = int(reg.group(1))
        from_left = int(reg.group(3))
        from_top = int(reg.group(4))
        width = int(reg.group(6))
        height = int(reg.group(7))
        for w in range(width):
            for h in range(height):
                pos = "{}x{}".format(from_left+w, from_top+h)
                if pos in claims:
                    if pos not in overlaps:
                        overlaps.add(pos)
                        sqin += 1
                else:
                    claims.add(pos)

print(sqin)

# day 3 part 2
claims = set()
overlaps = set()
nums = set()
claim_to_num = {}
overlapped_nums = set()
sqin = 0

with open("claims.txt", "r") as f:
    print("Working...")
    for line in f.readlines():
        reger = re.compile("#(\d+) @ ((\d+),(\d+)): ((\d+)x(\d+))")
        reg = reger.search(line)
        claim_num = int(reg.group(1))
        from_left = int(reg.group(3))
        from_top = int(reg.group(4))
        width = int(reg.group(6))
        height = int(reg.group(7))
        nums.add(claim_num)
        for w in range(width):
            for h in range(height):
                pos = "{}x{}".format(from_left+w, from_top+h)
                if pos in claims:
                    if pos not in overlaps:
                        overlaps.add(pos)
                        sqin += 1
                    try:
                        if claim_to_num[pos] not in overlapped_nums:
                            overlapped_nums.add(claim_to_num[pos])
                    except:
                        print("if you see this, frick")
                    overlapped_nums.add(claim_num)
                else:
                    claims.add(pos)
                    claim_to_num[pos] = claim_num

print(nums-overlapped_nums)