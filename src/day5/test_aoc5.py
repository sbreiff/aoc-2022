from aoc5 import *

test_case = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".split('\n')

expected_stacks = {'1': ['N', 'Z'], '2': ['D', 'C', 'M'], '3': ['P']}
expected_parsings = [
    ['1', '2', '1'],
    ['3', '1', '3'],
    ['2', '2', '1'],
    ['1', '1', '2']
]

def test_part1():
    stacks, _ = get_stacks(test_case)

    assert stacks == expected_stacks

    for i in range(len(expected_parsings)):
        assert parse_line(test_case[6 + i]) == expected_parsings[i]
        move_crate(stacks, *expected_parsings[i])

    assert stacks == {'1': ['C'], '2': ['M'], '3': ['Z', 'N', 'D', 'P']}

    assert get_message(stacks) == 'CMZ'


def test_part2():
    stacks, _ = get_stacks(test_case)

    assert stacks == expected_stacks

    for i in range(len(expected_parsings)):
        assert parse_line(test_case[6 + i]) == expected_parsings[i]
        move_crate(stacks, *expected_parsings[i], single=False)

    assert stacks == {'1': ['M'], '2': ['C'], '3': ['D', 'N', 'Z', 'P']}

    assert get_message(stacks) == 'MCD'


test_part1()
test_part2()
