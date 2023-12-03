nums = [str(n) for n in range(0, 10)]

print(nums)

with open('1/1.txt') as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        first = None
        last = None
        for c in line:
            if c in nums:
                if not first:
                    first = int(c)
                last = int(c)
        total += 10 * first
        total += last
    print(total)

