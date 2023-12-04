def find_nums(lines, line_num, col_num):
    nums = []
    i = line_num - 2
    while i < line_num + 1:
        i += 1
        if i >= len(lines):
            continue
        j = col_num - 2
        while j < col_num + 1:
            j += 1
            current_num = ''
            if lines[i][j].isnumeric():
                current_num = lines[i][j]
                
                for k in range(j-1, -1, -1):
                    if lines[i][k].isnumeric():
                        current_num = lines[i][k] + current_num
                    else:
                        break
                for k in range(j+1, len(lines[i])):
                    if lines[i][k].isnumeric():
                        current_num += lines[i][k]
                        j += 1
                    else:
                        break
                nums.append(int(current_num))
    return nums




with open('3/3.txt') as f:
    lines = f.readlines()
    total = 0

    for line_num, line in enumerate(lines):
        for i, char in enumerate(line):
            if char == '*':
                nums = find_nums(lines, line_num, i)
                if len(nums) == 2:
                    total += nums[0] * nums[1]
    
    print(total)