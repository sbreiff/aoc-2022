# Advent of Code - Day 3

import string
from sys import argv

def get_priority(letter):
    return string.ascii_letters.index(letter) + 1

def find_item_in_both_compartments(items):
    for letter in items:
        if letter in items[:len(items)//2] and letter in items[len(items)//2:]:
            return letter

def get_priority_sum_from_lines(lines):
    return sum([get_priority(find_item_in_both_compartments(line.rstrip('\n'))) for line in lines if line])

def find_badge(three_lines):
    for letter in three_lines[0]:
        if letter in three_lines[1] and letter in three_lines[2]:
            return letter

if __name__ == '__main__':
    with open(argv[1]) as input_file:
        text = input_file.readlines()
    print('Part 1 Answer:')
    print(get_priority_sum_from_lines(text))
    print('')
    print('Part 2 Answer:')
    print(sum([get_priority(find_badge(text[i*3:(i+1)*3])) for i in range(len(text)//3)]))

