# Advent of Code 2022 - Day 20


def move_num_in_sequence(i, num, sequence):
    idx = sequence.index((num, i))
    sequence.pop(idx)
    new_idx = idx + num
    if abs(new_idx) > len(sequence) - 1:
        new_idx = new_idx % (len(sequence))
    if new_idx == 0 and idx != 0:
        sequence.append((num, i))
    else:
        sequence.insert(new_idx, (num, i))
    return sequence


def all_moves(sequence, times=1, decrypt=1):
    new_sequence = [(sequence[i] * decrypt, i) for i in range(len(sequence))]
    for i in range(times):
        for j, num in enumerate(sequence):
            new_sequence = move_num_in_sequence(j, num * decrypt, new_sequence)
    return [item[0] for item in new_sequence]


def get_grove_coord_sum(final_sequence):
    idx = final_sequence.index(0)
    return sum(final_sequence[(idx + x) % len(final_sequence)] for x in [1000, 2000, 3000])


if __name__ == '__main__':
    with open('/Users/sb-7148/aoc2022/data/day20.txt') as infile:
        seq = [int(i) for i in infile.read().split() if i]
    print('Part 1 Answer:')
    print(get_grove_coord_sum(all_moves(seq)))
    print('')
    print('Part 2 Answer:')
    print(get_grove_coord_sum(all_moves(seq, times=10, decrypt=811589153)))