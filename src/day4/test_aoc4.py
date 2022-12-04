from aoc4 import *

test_cases = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".split()

parsed = [
    [[2, 4], [6, 8]],
    [[2, 3], [4, 5]],
    [[5, 7], [7, 9]],
    [[2, 8], [3, 7]],
    [[6, 6], [4, 6]],
    [[2, 6], [4, 8]]
]

expected = {
    1: [False, False, False, True, True, False],
    2: [False, False, True, True, True, True]
}


for i, case in enumerate(test_cases):
    p = parse_line(case)
    assert p == parsed[i]
    assert compare_assignments(*p) == expected[1][i]
    assert compare_assignments(*p, partial=True) == expected[2][i]