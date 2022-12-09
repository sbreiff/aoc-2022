# Advent of Code 2022 - Day 8

from sys import argv


def parse_rows(rows):
    return [[int(d) for d in row.rstrip('\n')] for row in rows if row.rstrip('\n')]


def find_visible_trees(trees):
    # trees = parse_rows(rows)
    return (len(trees) * len(trees[0])) - find_hidden_trees(trees)


def find_hidden_trees(tree_grid):
    # tree_grid = parse_rows(rows)
    hidden_trees = sum(
        is_hidden(i, j, tree_grid) 
        for i in range(0, len(tree_grid))
        for j in range(0, len(tree_grid[0]))
    )
    return hidden_trees


def is_hidden(row, col, grid):
    tree = grid[row][col]
    if row in (0, len(grid) - 1) or col in (0, len(grid[0]) - 1):
        return False
    if tree <= max(grid[row][:col]) and tree <= max(grid[row][col+1:]):
        column = [r[col] for r in grid]
        if tree <= max(column[:row]) and tree <= max(column[row+1:]):
            return True
    return False


def scenic_score(row, col, grid):
    if row in [0, len(grid)] or col in [0, len(grid[0])]:
        return 0
    tree = grid[row][col]
    column = [tree_row[col] for tree_row in grid]
    # up
    u = get_view_distance(tree, column[:row][::-1])
    # down
    d = get_view_distance(tree, column[row+1:])
    # left
    l = get_view_distance(tree, grid[row][:col][::-1])
    # right
    r = get_view_distance(tree, grid[row][col+1:])
    return u * d * l * r


def get_view_distance(val, tree_list):
    blocked = [True if tree >= val else False for tree in tree_list]
    if True in blocked:
        return blocked.index(True) + 1
    return len(blocked)


def best_scenic_score(tree_grid):
    best_score = max(
        scenic_score(i, j, tree_grid) 
        for i in range(0, len(tree_grid))
        for j in range(0, len(tree_grid[0]))
    )
    return best_score


if __name__ == '__main__':
    input_file = '/Users/sb-7148/aoc2022/data/day8.txt' if len(argv) < 2 else argv[1]
    with open(input_file) as infile:
        lines = infile.readlines()
    trees = parse_rows(lines)
    print('Part 1 Answer:')
    print(find_visible_trees(trees))
    print('')
    print('Part 2 Answer:')
    print(best_scenic_score(trees))