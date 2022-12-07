# Advent of Code 2022 - Day 7

from sys import argv


def parse_input(lines):
    parsed = {}
    path = []
    # cwd = ''
    # parent = None
    for line in lines:
        if line.startswith('$ cd'):
            if not '..' in line:
                path.append(line.split()[-1])
                parsed['/'.join(path)] = []
            else:
                path = path[:-1]
        elif line.startswith('$ ls'):
            continue
        elif path and line:
            if line.startswith('dir'):
                line = 'dir ' + '/'.join(path + [line.split()[-1]])
            parsed['/'.join(path)].append(line)
    return parsed


def get_directory_size(fs_dict, dirname):
    size = 0
    for item in fs_dict[dirname]:
        if item.startswith('dir '):
            size += get_directory_size(fs_dict, item.split()[-1])
        else:
            size += int(item.split()[0])
    return size


def get_all_directory_sizes(fs_dict):
    return {dirname: get_directory_size(fs_dict, dirname) for dirname in fs_dict.keys()}


def get_final_sum(size_dict):
    return sum(val for val in size_dict.values() if val <= 100000)


def get_delete_size(size_dict):
    return 30000000 - (70000000 - size_dict['/'])

def get_size_to_delete(size_dict, delete_size):
    return sorted(val for val in size_dict.values() if val > delete_size)[0]


if __name__ == '__main__':
    input_file = '/Users/sb-7148/aoc2022/data/day7.txt' if len(argv) < 2 else argv[1]
    with open(input_file) as infile:
        lines = infile.readlines()
    all_sizes = get_all_directory_sizes(parse_input(lines))
    print('Part 1 Answer:')
    print(get_final_sum(all_sizes))
    print('')
    print('Part 2 Answer:')
    print(get_size_to_delete(all_sizes, get_delete_size(all_sizes)))