lines = list(open('5/5.txt'))
seeds = []
maps = []

for line in lines:
    if line == '\n':
        continue
    if 'seeds: ' in line:
        seeds = [int(x.strip()) for x in line.replace('seeds: ', '').split(' ')]    
    elif 'map:' in line:
        maps.append([])
    else:
        maps[len(maps) - 1].append([int(x.strip()) for x in line.split(' ')])

# the destination range start, the source range start, and the range length.
lowest = None    
for seed in seeds:
    for map_set in maps:
        for map in map_set:
            if seed >= map[1] and seed < map[1] + map[2]:
                seed = map[0] + (seed - map[1])
                break
    if lowest is None or seed < lowest:
        lowest = seed

print(lowest)