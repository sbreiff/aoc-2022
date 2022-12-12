# Advent of Code 2022 - Day 11

from operator import add, mul, pow
from math import prod


def parse_input(text):
    monkeys = [[line.strip() for line in section.split('\n') if line] 
               for section in text.split('Monkey') if ''.join(section)]
    monkey_dict = {}
    for monkey in monkeys:
        if not monkey:
            continue
        k = int(monkey[0][:monkey[0].index(':')])
        items = [int(num.strip()) for num in monkey[1][monkey[1].index(':')+1:].split(',')]
        operation = monkey[2][monkey[2].index('old')+4:]
        if operation.startswith('* old'):
            k_op = [pow, 2]
        else:
            num = int(operation.split()[-1].strip())
            if operation.startswith('+'):
                k_op = [add, num]
            elif operation.startswith('*'):
                 k_op = [mul, num]
        test = [int(line.split()[-1].strip()) for line in monkey[3:6]]
        monkey_dict[k] = {
            'items': items,
            'operation': k_op,
            'test': test,
            'inspected': 0
        }
    return monkey_dict


def monkey_turn(monkey, monkey_dict, divisor=3):
    lcm = prod([v['test'][0] for v in monkey_dict.values()])
    curr_monkey = monkey_dict[monkey]
    for item in curr_monkey['items']:
        new_item = curr_monkey['operation'][0](item, curr_monkey['operation'][1])
        curr_monkey['inspected'] += 1
        new_item = new_item // divisor
        if divisor == 1:
            new_item = new_item % lcm
        if new_item % curr_monkey['test'][0]:
            monkey_dict[curr_monkey['test'][2]]['items'].append(new_item)
        else:
            monkey_dict[curr_monkey['test'][1]]['items'].append(new_item)
    monkey_dict[monkey]['items'] = []
    return monkey_dict


def monkey_round(monkey_dict, divisor=3):
    for i in range(len(monkey_dict.keys())):
        new_dict = monkey_turn(i, monkey_dict, divisor)
    return new_dict


def find_active_monkeys(monkey_dict, rounds=20, divisor=3):
    for i in range(rounds):
        monkey_dict = monkey_round(monkey_dict, divisor)
    result = sorted([(k, v['inspected']) for k, v in monkey_dict.items()], 
                    key=lambda x: monkey_dict[x[0]]['inspected'])
    return result[-1][1] * result[-2][1]


if __name__ == '__main__':
    input_file = '/Users/sb-7148/aoc2022/data/day11.txt'
    with open(input_file) as infile:
        text = infile.read()
    monkeys = parse_input(text)
    print(find_active_monkeys({k: v for k, v in monkeys.items()}))
    print('')
    monkeys = parse_input(text)
    print(find_active_monkeys(monkeys, rounds=10000, divisor=1))