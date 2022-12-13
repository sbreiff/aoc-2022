from aoc13 import *


test_case = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".split('\n')

# test parse_input
assert len(parse_input(test_case)) == 8
assert len(parse_input(test_case, pairs=False)) == 16

example_data = parse_input(test_case)

# test compare_nums
assert compare_nums(1, 2) == -1
assert compare_nums(4, 3) == 1
assert compare_nums(5, 5) == 0

# test compare_lists
assert compare_lists([1, 2, 2], [2, 2, 2]) == -1
assert compare_lists([2, 2, 2], [1, 2, 2]) == 1
assert compare_lists([1, 2, 3], [1, 2]) == 1
assert compare_lists([1, 2, 3], [1, 2, 3, 4]) == -1
assert compare_lists(*example_data[0]) == -1
assert compare_lists(*example_data[1]) == -1
assert compare_lists(*example_data[2]) == 1
assert compare_lists(*example_data[3]) == -1
assert compare_lists(*example_data[4]) == 1
assert compare_lists(*example_data[5]) == -1
assert compare_lists(*example_data[6]) == 1
assert compare_lists(*example_data[7]) == 1

assert find_pairs_in_correct_order(test_case) == [1, 2, 4, 6]

assert reorder_packets(parse_input(test_case, pairs=False)) == [
    [],
    [[]],
    [[[]]],
    [1,1,3,1,1],
    [1,1,5,1,1],
    [[1],[2,3,4]],
    [1,[2,[3,[4,[5,6,0]]]],8,9],
    [1,[2,[3,[4,[5,6,7]]]],8,9],
    [[1],4],
    [3],
    [[4,4],4,4],
    [[4,4],4,4,4],
    [7,7,7],
    [7,7,7,7],
    [[8,7,6]],
    [9]
]

assert get_product(test_case) == 140
