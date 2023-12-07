import math


lines = list(open('6/6.txt'))

time = int(lines[0].replace('Time:', '').replace(' ', ''))
record_distance = int(lines[1].replace('Distance:', '').replace(' ', ''))


def get_record_perm_count(time, record_distance):
    for i in range(0, math.ceil(time / 2)):
        distance = i * (time - i)
        if distance > record_distance:
            return (time + 1) - (i * 2)
    return 0    


count = get_record_perm_count(time, record_distance)
print(count)