# Advent of Code 2022 - Day 12

from string import ascii_lowercase
from anytree import Node, RenderTree
from anytree.search import findall


def get_destination(data):
    for i in range(len(data)):
        if 'E' in data[i]:
            return (i, data[i].index('E'))


def is_valid_height(val1, val2):
    if val1 == 'E':
        return False
    use_val1 = 'a' if val1 == 'S' else val1
    use_val2 = 'a' if val2 == 'S' else val2
    if ascii_lowercase.index(use_val2) > ascii_lowercase.index(use_val1) + 1:
        return False
    return True


def get_next_step(row, col, parent_val, data):
    next_val = data[row][col]
    if is_valid_height(next_val, parent_val):
        return (row, col, next_val)
    return None


def add_nodes(data, visited, queue, found=False, start_val='S'):
    parent_node = queue.pop(0)
    if (parent_node.i, parent_node.j) in visited:
        return found
    val = data[parent_node.i][parent_node.j]
    if val == start_val:
        found = True
        return found
    if val == 'E':
        val = 'z'
    up = None
    down = None
    left = None
    right = None
    if parent_node.i > 0:
        up = get_next_step(parent_node.i - 1, parent_node.j, val, data)
    if parent_node.i < len(data) - 1:
        down = get_next_step(parent_node.i + 1, parent_node.j, val, data)
    if parent_node.j > 0:
        left = get_next_step(parent_node.i, parent_node.j - 1, val, data)
    if parent_node.j < len(data[0]) - 1:
        right = get_next_step(parent_node.i, parent_node.j + 1, val, data)
    visited.append((parent_node.i, parent_node.j))
    next_steps = [item for item in [up, down, left, right] if item]
    for item in next_steps:
        if item and item[2] == start_val:
            start = Node(start_val, parent=parent_node)
            found = True
            return found
    for item in next_steps:
        next_coord = (item[0], item[1])
        if next_coord not in visited:
            next_node = Node(f"{item[0]},{item[1]}", i=item[0], j=item[1], parent=parent_node)
            if next_node not in queue:
                queue.append(next_node)
    return found
    

def build_tree(data, start_val='S'):
    data = [line.rstrip('\n') for line in data if line.rstrip('\n')]
    dest = get_destination(data)
    visited_coords = []
    root = Node(f"{dest[0]},{dest[1]}", i=dest[0], j=dest[1])
    queue = [root]
    found = False
    while not found:
        found = add_nodes(data, visited_coords, queue, found=found, start_val=start_val)
    solutions = findall(root, filter_=lambda node: node.name == start_val)
    if not solutions:
        return
    return min([len(node.path) - 1 for node in solutions])


if __name__ == '__main__':
    with open('/Users/sb-7148/aoc2022/data/day12.txt') as input_file:
        text = input_file.readlines()
    print('Part 1 Answer:')
    print(build_tree(text))
    print('')
    print('Part 2 Answer:')
    print(build_tree(text, start_val='a'))