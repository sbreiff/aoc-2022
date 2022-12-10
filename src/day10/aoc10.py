# Advent of Code 2022 - Day 10


def run_instruction(x_list, instruction):
    x_list.append(x_list[-1])
    if instruction.startswith('addx'):
        v = instruction.rstrip('\n').split()[-1]
        x_list.append(x_list[-1] + int(v))
    return x_list


def run_all(data, max_length=250):
    x_list = [1]
    idx = 0
    while len(x_list) < max_length:
        if idx > len(data) - 1:
            break
        x_list = run_instruction(x_list, data[idx])
        idx += 1
    return x_list


def get_x(cycle, x_list):
    return x_list[cycle - 1] * cycle


def get_all_x(x_list, cycles=[]):
    if not cycles:
        cycles = [i * 20 for i in range(1, 12)][0::2]
    return [get_x(cycle, x_list) for cycle in cycles]


def print_pixels(x_list):
    rows = []
    for i in range(6):
        pixels = []
        for j in range(40):
            idx = (i*40) + j
            a = x_list[idx]
            if j in (a-1, a, a+1):
                pixels.append('#')
            else:
                pixels.append('.')
        rows.append(pixels)
    return [''.join(row) for row in rows]


if __name__ == '__main__':
    input_file = '/Users/sb-7148/aoc2022/data/day10.txt'
    with open(input_file) as infile:
        lines = infile.readlines()
    x_vals = run_all([line for line in lines if line])
    print('Part 1 Answer:')
    print(sum(get_all_x(x_vals)))
    print('')
    print('Part 2 Answer:')
    for row in print_pixels(x_vals):
        print(row)

