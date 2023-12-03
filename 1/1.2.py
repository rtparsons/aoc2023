def generate_nums():
    return [str(n) for n in range(0, 10)]


def get_num(to_search):
    for n in nums:
        if n in to_search:
            return int(n)
    
    for n in spelt_nums:
        if n[0] in to_search:
            return n[1]
    
    return None


nums = generate_nums()
spelt_nums  = [('zero', 0), ('one', 1), ('two', 2), ('three', 3), ('four', 4), 
                  ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]

with open('1/1.txt') as f:
    total = 0
    lines = f.readlines()
    counter = 0
    for line in lines:
        counter += 1
        left = None
        right = None
        current_word = ''
        for c in line:
            current_word += c
            if left := get_num(current_word):
                break
        
        current_word = ''
        for c in line[::-1]:
            current_word = c + current_word
            if right := get_num(current_word):
                break
            
        total += 10 * left
        total += right

        print(f'{line} - {left} - {right}')
    print(total)

