from aoc20 import *


test_case = """
1
2
-3
3
-2
0
4
""".split()


expected_results = [
    [2, 1, -3, 3, -2, 0, 4],
    [1, -3, 2, 3, -2, 0, 4],
    [1, 2, 3, -2, -3, 0, 4],
    [1, 2, -2, -3, 0, 3, 4],
    [1, 2, -3, 0, 3, 4, -2],
    [1, 2, -3, 0, 3, 4, -2],
    [1, 2, -3, 4, 0, 3, -2]
]


example_sequence = [int(num) for num in test_case if num]

new_sequence = [(example_sequence[i], i) for i in range(len(example_sequence))]

for i, num in enumerate(example_sequence):
    new_sequence = move_num_in_sequence(i, num, new_sequence)
    assert [item[0] for item in new_sequence] == expected_results[i]

final_seq_1 = all_moves(example_sequence)
assert final_seq_1 == expected_results[-1]
assert get_grove_coord_sum(final_seq_1) == 3

final_seq_2 = all_moves(example_sequence, times=10, decrypt=811589153)
assert final_seq_2 == [0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153]
assert get_grove_coord_sum(final_seq_2) == 1623178306