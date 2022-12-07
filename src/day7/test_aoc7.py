from aoc7 import *


test_case = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".split('\n')

expected_results = {
    '/': 48381165,
    '//a': 94853,
    '//d': 24933642,
    '//a/e': 584
}


dirs = parse_input(test_case)

assert set(dirs.keys()) == set(expected_results.keys())

all_sizes = get_all_directory_sizes(dirs)

for dir, size in all_sizes.items():
    assert size == expected_results[dir]

assert get_final_sum(all_sizes) == 95437

assert get_delete_size(all_sizes) == 8381165

assert get_size_to_delete(all_sizes, get_delete_size(all_sizes)) == 24933642
