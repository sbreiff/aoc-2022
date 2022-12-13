# Advent of Code 2022 - Day 13

import ast
from functools import cmp_to_key


def compare_nums(left, right):
    if left < right:
        return -1
    elif right < left:
        return 1
    else:
        return 0


def compare_lists(list1, list2):
    lists = [list1, list2]
    correct = None
    for i in range(max(len(lst) for lst in lists)):
        if i == len(list1):
            correct = -1
            break
        elif i == len(list2):
            correct = 1
            break
        l = list1[i]
        r = list2[i]
        if all(isinstance(item, int) for item in [l, r]):
            # compare nums
            if l == r:
                continue
            else:
                correct = compare_nums(l, r)
        else:
            if isinstance(l, list) and isinstance(r, int):
                correct = compare_lists(l, [r])
            elif isinstance(l, int) and isinstance(r, list):
                correct = compare_lists([l], r)
            else:
                correct = compare_lists(l, r)
        if correct:
            break
    return correct


def parse_input(lines, pairs=True):
    if not lines[0]:
        lines = lines[1:]
    if pairs:
        return [
            [ast.literal_eval(lines[i]), ast.literal_eval(lines[i+1])] 
            for i in range(0, len(lines) - 2, 3)
        ]
    else:
        return [ast.literal_eval(line) for line in lines if line.rstrip('\n')]


def find_pairs_in_correct_order(data):
    pairs = parse_input(data)
    return [i + 1 for i, pair in enumerate(pairs) if compare_lists(*pair) == -1]


def reorder_packets(packets):
    packets.sort(key=cmp_to_key(compare_lists))
    return packets


def get_product(data):
    all_packets = parse_input(data, pairs=False)
    divider1, divider2 = [[2]], [[6]]
    all_packets.append(divider1)
    all_packets.append(divider2)
    reordered = reorder_packets(all_packets)
    return (reordered.index(divider1) + 1) * (reordered.index(divider2) + 1)


if __name__ == '__main__':
    with open('/Users/sb-7148/aoc2022/data/day13.txt') as infile:
        lines = infile.readlines()
    print('Part 1 Answer:')
    print(sum(find_pairs_in_correct_order(lines)))
    print('Part 2 Answer:')
    print(get_product(lines))
    