def parse_line(line):
    line = line.split(': ')[1].strip()
    return [set(int(y.strip()) for y in x.split(' ') if y) for x in line.split('|')]

lines = list(open('4/4.txt'))

res = 0
for line in lines:
    parsed_line = parse_line(line)
    winners = parsed_line[0].intersection(parsed_line[1])
    res += (2 ** (len(winners) - 1)) if len(winners) else 0
print(res)