def parse_line(line):
    game_no = int(line[5:line.index(':')])
    line = line[line.index(':') + 2:]
    games = line.split(';')
    res = []
    for game in games:
        cubes = [x.strip().split(' ') for x in game.split(',')]
        res.append({x[1]: int(x[0]) for x in cubes})

    return game_no, res


def get_line_value(parsed_line):
    #12 red cubes, 13 green cubes, and 14 blue cubes?
    for game in parsed_line[1]:
        if game.get('red', 0) > 12 or game.get('green', 0) > 13 or game.get('blue', 0) > 14:
            return 0
    return parsed_line[0]


with open('2/2.txt') as f:
    lines = f.readlines()

    total = 0
    for line in lines:
        parsed_line = parse_line(line)
        total += get_line_value(parsed_line)
    print(total)