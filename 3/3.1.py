def find_symbol(lines, start_line, start_col, width):
    for line_num in range(start_line, start_line + 3):
        if line_num >= len(lines):
            continue
        line = lines[line_num]
        for i in range(start_col, start_col + width):
            if i > len(line):
                continue
            char = line[i]
            if not char.isnumeric() and char != '.' and char != '\n':
                return True
    return False


with open('3/3.txt') as f:
    lines = f.readlines()
    total = 0

    for line_num, line in enumerate(lines):
        current_num = ''
        for i, char in enumerate(line):
            if char.isnumeric():
                current_num += char
            elif current_num:
                if find_symbol(lines, line_num - 1, i - (len(current_num) + 1), len(current_num) + 2):
                    print(int(current_num))
                    total += int(current_num)
                current_num = ''
    
    print(total)