# Advent of Code 2022 - day 2
# input file at ../../data/day2.txt


from sys import argv


rps_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}


def get_points_from_round(opponent_choice, player_choice):
    points = 0
    if opponent_choice == player_choice:
        points = 3
    else:
        result = player_choice - opponent_choice
        if result % 3 == 1:
            points = 6
        else:
            points = 0
    return points + player_choice


def get_points_encrypted_part1(opponent, player):
    return get_points_from_round(rps_dict[opponent], rps_dict[player])


def get_points_encrypted_part2(opponent, player):
    player_choice = (rps_dict[opponent] + rps_dict[player] - 2) % 3
    if player_choice == 0:
        player_choice = 3
    return get_points_from_round(rps_dict[opponent], player_choice)


def get_points_from_file(infile, part=1):
    total = 0
    with open(infile) as input_f:
        lines = input_f.readlines()
    for line in lines:
        if line:
            choices = line.rstrip('\n').split()
            if part == 1:
                total += get_points_encrypted_part1(choices[0], choices[1])
            elif part == 2:
                total += get_points_encrypted_part2(choices[0], choices[1])

    return total


if __name__ == '__main__':
    print('Part 1 Answer:')
    print(get_points_from_file(argv[1], part=1))
    print('')
    print('Part 2 Answer:')
    print(get_points_from_file(argv[1], part=2))