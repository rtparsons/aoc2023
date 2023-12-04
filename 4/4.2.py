from dataclasses import dataclass


node_count = 0


@dataclass
class Node:
    node_num: str
    children: list

    def __str__(self) -> str:
        for child in self.children:
            print(child)
        return str(self.node_num)


def parse_line(line):
    line = line.split(': ')[1].strip()
    return [set(int(y.strip()) for y in x.split(' ') if y) for x in line.split('|')]


def build_tree(lines, i, is_winner) -> Node:
    if i >= len(lines):
        return None
    global node_count
    node_count += 1
    if node_count  % 100 == 0:
        print(f'{node_count} - {i}')
    parsed_line = parse_line(lines[i])
    winners = parsed_line[0].intersection(parsed_line[1])
    res = Node(node_num=i, children=[])
    if not is_winner:
        res.children.append(build_tree(lines, i + 1, False))
    for j in range(0, len(winners)):
        res.children.append(build_tree(lines, i + j + 1, True))
    res.children = [x for x in res.children if x]
    return res


def branch_count(node: Node):
    count = 1
    for child in node.children:
        count += branch_count(child)
    return count

lines = list(open('4/4.txt'))

tree = build_tree(lines, 0, False)

res = branch_count(tree)

print(res)
