from aoc2 import *


test_cases = {
    'Part 1': {('A', 'Y'): 8, ('B', 'X'): 1, ('C', 'Z'): 6},
    'Part 2a': {('A', 'Y'): 4, ('B', 'X'): 1, ('C', 'Z'): 7},
    'Part 2b': {
        ('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8, 
        ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9, 
        ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7
    }
}


print('Testing Part 1...')
for k, v in test_cases['Part 1'].items():
        assert get_points_encrypted_part1(*k) == v
print('Success!')

for part in ['Part 2a', 'Part 2b']:
    print(f'Testing {part}:...')
    for k, v in test_cases[part].items():
        assert get_points_encrypted_part2(*k) == v
    print('Success!')