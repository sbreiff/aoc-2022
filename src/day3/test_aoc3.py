from aoc3 import *

test_case = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".split()

expected_results_part1 = [16, 38, 42, 22, 20, 19]

expected_results_part2 = {0: ('r', 18), 1: ('Z', 52)}


for i, expected in enumerate(expected_results_part1):
    assert get_priority(find_item_in_both_compartments(test_case[i])) == expected


assert get_priority_sum_from_lines(test_case) == sum(expected_results_part1) == 157


summed = 0
for i, grp in enumerate([test_case[:3], test_case[3:]]):
    badge = find_badge(grp)
    priority = get_priority(badge)
    assert badge == expected_results_part2[i][0]
    assert priority == expected_results_part2[i][1]
    summed += priority
assert summed == sum([item[1] for item in expected_results_part2.values()])