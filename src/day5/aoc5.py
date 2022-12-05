# Advent of Code 2022 - Day 5

from sys import argv


def get_stacks(lines):
    idx = None
    for i, line in enumerate(lines):
        if '1' in line:
            idx = i
            break
    stack_dict = {num: [] for num in lines[i].rstrip('\n').split()}
    idx_dict = {num: lines[i].index(num) for num in stack_dict.keys()}
    for line in lines[:i]:
        if line:
            for num in stack_dict.keys():
                if idx_dict[num] < len(line):
                    val = line[idx_dict[num]].strip()
                    if val:
                        stack_dict[num].append(line[idx_dict[num]])
    return stack_dict, idx


def move_crate(stacks, qty, old_col, new_col, single=True):
    if single:
        for i in range(int(qty)):
            stacks[new_col] = [stacks[old_col].pop(0)] + stacks[new_col]
    else:
        stacks[new_col] = stacks[old_col][:int(qty)] + stacks[new_col]
        stacks[old_col] = stacks[old_col][int(qty):]


def get_message(stacks):
    return ''.join([stacks[str(i+1)][0] for i in range(len(stacks.keys()))])


def parse_line(line):
    return [item for item in line.rstrip('\n').split() if any(d in item for d in '0123456789')]


if __name__ == '__main__':
    with open(argv[1]) as infile:
        lines = infile.readlines()
    parts = {'1': True, '2': False}
    for part, single_val in parts.items():
        print(f'Part {part} Answer:')
        stacks, i = get_stacks(lines)
        for line in lines[i+1:]:
            if line.strip():
                move_crate(stacks, *parse_line(line), single=single_val)
        print(get_message(stacks))
        print('')

