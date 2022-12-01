# aoc 2022

from sys import argv

input_file = argv[1]

def order_elves_by_cals(infile):
    with open(infile) as input_f:
        text = input_f.read()
    cals = [[int(num) for num in elf.split('\n') if num] for elf in text.split('\n\n')]
    cal_dict = {i + 1: sum(v) for i, v in enumerate(cals)}
    ordered = sorted(cal_dict.items(), key=lambda x: x[1])
    return ordered

def get_max_cals(input_dict):
    return input_dict[-1][-1]

def get_cals_from_top_three(input_dict):
    return sum(item[1] for item in input_dict[-3:])

def print_output(infile):
    elves = order_elves_by_cals(infile)
    print('Part 1:')
    print(get_max_cals(elves))
    print('\n')
    print('Part 2:')
    print(get_cals_from_top_three(elves))
    
print_output(input_file)

