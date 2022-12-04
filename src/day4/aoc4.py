# Advent of Code - Day 4

from sys import argv


def compare_assignments(assn1, assn2, partial=False):
    comparators = [-1, 0] if partial else [0, -1]
    if assn1[0] <= assn2[comparators[0]] and assn1[-1] >= assn2[comparators[1]]:
        return True
    elif assn2[0] <= assn1[comparators[0]] and assn2[-1] >= assn1[comparators[1]]:
        return True
    return False


def parse_line(line):
    return [[int(num) for num in assn.split('-')] for assn in line.rstrip('\n').split(',')]


if __name__ == '__main__':
    with open(argv[1]) as input_file:
        lines = input_file.readlines()
    parsed_lines = [parse_line(l) for l in lines]
    print('Part 1 Answer:')
    print(sum(compare_assignments(*line) for line in parsed_lines))
    print('')
    print('Part 2 Answer:')
    print(sum(compare_assignments(*line, partial=True) for line in parsed_lines))