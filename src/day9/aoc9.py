# Advent of Code 2022 - Day 9

from sys import argv


def move_rope(direction, knot_list):
    if direction.lower() == 'r':
        knot_list[0][0] += 1
    if direction.lower() == 'l':
        knot_list[0][0] += -1
    if direction.lower() == 'u':
        knot_list[0][1] += -1
    if direction.lower() == 'd':
        knot_list[0][1] += 1
    for i in range(len(knot_list) - 1):
        diff = [knot_list[i][0] - knot_list[i+1][0], knot_list[i][1] - knot_list[i+1][1]]
        for j in (0, 1):
            if abs(diff[j]) == 2:
                knot_list[i+1][j] += diff[j]//2
                if abs(diff[1-j]) == 1:
                    knot_list[i+1][1-j] += diff[1-j]
                elif abs(diff[1-j]) == 2:
                    knot_list[i+1][1-j] += diff[1-j]//2
                break
    return knot_list


def all_moves(lines, num_knots=2):
    knots = [[0,0] for i in range(num_knots)]
    all_positions = []
    for line in [l.rstrip('\n').split() for l in lines if l.rstrip('\n')]:
        for i in range(int(line[1])):
            knots = move_rope(line[0], knots)
            if knots[-1] not in all_positions:
                all_positions.append([pos for pos in knots[-1]])
    return len(all_positions)


if __name__ == '__main__':
    input_file = '/Users/sb-7148/aoc2022/data/day9.txt' if len(argv) < 2 else argv[1]
    with open(input_file) as infile:
        data = infile.readlines()
    print('Part 1 Answer:')
    print(all_moves(data))
    print('')
    print('Part 2 Answer:')
    print(all_moves(data, num_knots=10))