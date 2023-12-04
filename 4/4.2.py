def parse_line(line):
    line = line.split(': ')[1].strip()
    return [set(int(y.strip()) for y in x.split(' ') if y) for x in line.split('|')]


lines = list(open('4/4.txt'))
scores = [1 for _ in lines]

for i, line in enumerate(lines):
    parsed_line = parse_line(line)
    winners = parsed_line[0].intersection(parsed_line[1])
    
    for j in range(1, len(winners) + 1):
        scores[i + j] += scores[i]

print(scores)
print(sum(scores))