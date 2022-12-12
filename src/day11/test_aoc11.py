from aoc11 import *


example_input = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

expected_dict = {
    0: {
        'items': [79, 98],
        'operation': [mul, 19],
        'test': [23, 2, 3]
    },
    1: {
        'items': [54, 65, 75, 74],
        'operation': [add, 6],
        'test': [19, 2, 0]
    },
    2: {
        'items': [79, 60, 97],
        'operation': [pow, 2],
        'test': [13, 1, 3]
    },
    3: {
        'items': [74],
        'operation': [add, 3],
        'test': [17, 0, 1]
    }
}

monkeys = parse_input(example_input)

for i, monkey in enumerate(monkeys.values()):
    for k in ['items', 'test', 'operation']:
        assert monkey[k] == expected_dict[i][k]

assert find_active_monkeys(monkeys) == 10605

monkeys = parse_input(example_input)
assert find_active_monkeys(monkeys, rounds=10000, divisor=1) == 2713310158

