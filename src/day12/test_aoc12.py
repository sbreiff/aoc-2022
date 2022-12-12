from aoc12 import *


test_case = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".split('\n')


# test get_destination
data = [line.rstrip('\n') for line in test_case if line.rstrip('\n')]
assert get_destination(data) == (2, 5)

# test is_valid_height
assert is_valid_height('a', 'b')
assert not is_valid_height('E', 'x')
assert not is_valid_height('a', 'c')
assert is_valid_height('S', 'a')
assert not is_valid_height('S', 'c')
assert is_valid_height('z', 'm')

# test get_next_step
assert not get_next_step(1, 7, 'x', data)
assert get_next_step(1, 5, 'x', data) == (1, 5, 'x')

# test build_tree
assert build_tree(data) == 31
assert build_tree(data, start_val='a') == 29