from aoc9 import *


test_case = '''
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''.split('\n')

test_case_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".split('\n')

example_knots = [
    [5, -3], [5, -2], [4, -1], [3, -1], [2, -1], [1, -1], [0, 0], [0, 0], [0, 0], [0, 0]
]

expected_knots = [
    [5, -4], [5, -3], [5, -2], [4, -2], [3, -2], [2, -2], [1, -1], [0, 0], [0, 0], [0, 0]
]

assert move_rope('u', example_knots) == expected_knots

assert all_moves(test_case) == 13
assert all_moves(test_case_2, 10) == 36

assert move_rope('l', [[3, -4], [4, -3]]) == [[2, -4], [3, -4]]