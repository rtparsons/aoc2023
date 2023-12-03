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
    combined_dict = {}
    for game in parsed_line[1]:
        for k, v in game.items():
            if k not in combined_dict or combined_dict[k] < v:
                combined_dict[k] = v
    
    if len(combined_dict) < 3:
        return 0
    return combined_dict['red'] * combined_dict['blue'] * combined_dict['green']


with open('2/2.txt') as f:
    lines = f.readlines()

    total = 0
    for line in lines:
        parsed_line = parse_line(line)
        total += get_line_value(parsed_line)
    print(total)
