from aoc6 import *

test_cases = {
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb': (7, 19),
    'bvwbjplbgvbhsrlpgdmjqwftvncz': (5, 23),
    'nppdvjthqldpwncqszvftbrmjlhg': (6, 23),
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg': (10, 29),
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw': (11, 26)
}

for msg, val in test_cases.items():
    assert find_marker(msg) == val[0]
    assert find_marker(msg, l=14) == val[1]