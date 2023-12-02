from typing import IO
import re

R_COLOUR = '(\d+) (blue|red|green)'


def part1(f: IO):
    sum = 0
    r_id = 'Game (\d+)'
    limits = {'red': 12, 'green': 13, 'blue': 14}

    for line in f.readlines():
        id = int(re.search(r_id, line).group(1))
        amounts = re.findall(R_COLOUR, line)

        for amount in amounts:
            if int(amount[0]) > limits[amount[1]]:
                break
        else:
            sum += id

    return sum


def part2(f: IO):
    sum = 0

    for line in f.readlines():
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        amounts = re.findall(R_COLOUR, line)

        for amount in amounts:
            min_cubes[amount[1]] = int(amount[0]) if int(amount[0]) > min_cubes[amount[1]] else min_cubes[amount[1]]

        sum += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    return sum


if __name__ == '__main__':
    with open('Day2/input.txt', 'r') as f:
        print(f'Part 1: {part1(f)}')
    with open('Day2/input.txt', 'r') as f:
        print(f'Part 2: {part2(f)}')
