lines = list(open('5/5.txt'))
seeds = []
maps = []

for line in lines:
    if line == '\n':
        continue
    if 'seeds: ' in line:
        temp_seeds = [int(x.strip()) for x in line.replace('seeds: ', '').split(' ')]
        temp_seeds = [temp_seeds[i:i + 2] for i in range(0, len(temp_seeds), 2)]
        for seed in temp_seeds:
            i = seed[0]
            while i < seed[0] + seed[1]:
                seeds.append([i, i])
                i += 10000
    elif 'map:' in line:
        maps.append([])
    else:
        maps[len(maps) - 1].append([int(x.strip()) for x in line.split(' ')])

# once i found the approx range, loop through to find the exact result
# seeds = [[x, x] for x in range(3521060627, 3521070627)]

# the destination range start, the source range start, and the range length.
lowest = None    
for seed in seeds:
    for map_set in maps:
        for map in map_set:
            if seed[0] >= map[1] and seed[0] < map[1] + map[2]:
                seed[0] = map[0] + (seed[0] - map[1])
                break
    if lowest is None or seed[0] < lowest[0]:
        lowest = seed

print(lowest)