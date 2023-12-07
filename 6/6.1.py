import math


lines = list(open('6/6.txt'))

times = [int(x.strip()) for x in lines[0].replace('Time:', '').split(' ') if x.strip()]
distances = [int(x.strip()) for x in lines[1].replace('Distance:', '').split(' ') if x.strip()]


def get_record_perm_count(time, record_distance):
    for i in range(0, math.ceil(time / 2)):
        distance = i * (time - i)
        if distance > record_distance:
            return (time + 1) - (i * 2)
    return 0    

counts = []
for time, record_distance in zip(times, distances):
    count = get_record_perm_count(time, record_distance)
    counts.append(count)
print(math.prod(counts))