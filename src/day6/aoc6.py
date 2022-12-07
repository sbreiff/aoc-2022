# Advent of Code 2022 - Day 6

from sys import argv


def find_marker(buffer, l=4):
    for i in range(l, len(buffer)):
        start = buffer[i-l:i]
        if len(start) == len(set(start)):
            return i


if __name__ == '__main__':
    input_file = '/Users/sb-7148/aoc2022/data/day6.txt' if len(argv) == 1 else argv[1]
    with open(input_file) as infile:
        text = infile.read()
    print('Part 1 Answer:')
    print(find_marker(text))
    print('')
    print('Part 2 Answer:')
    print(find_marker(text, l=14))