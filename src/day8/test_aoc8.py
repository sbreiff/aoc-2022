from aoc8 import *

test_case = """
30373
25512
65332
33549
35390
""".split('\n')

trees = parse_rows(test_case)
assert trees == [
    [3, 0, 3, 7, 3], 
    [2, 5, 5, 1, 2], 
    [6, 5, 3, 3, 2], 
    [3, 3, 5, 4, 9], 
    [3, 5, 3, 9, 0]
]

assert is_hidden(1,1, trees) == False
assert is_hidden(1,2, trees) == False
assert is_hidden(1,3, trees) == True
assert is_hidden(2,1, trees) == False
assert is_hidden(2,2, trees) == True
assert is_hidden(2,3, trees) == False
assert is_hidden(3,3, trees) == True
assert is_hidden(3,2, trees) == False
assert is_hidden(3,4, trees) == False

assert find_visible_trees(trees) == 21

assert scenic_score(1, 2, trees) == 4
assert scenic_score(3, 2, trees) == 8

assert best_scenic_score(trees) == 8