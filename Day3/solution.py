import re


def part1(lines):
    sum = 0

    r_symbol = re.compile(r'([^\d.\n])')
    r_numbers = re.compile(r'(\d+)')

    symbols = []
    numbers = []

    for i, line in enumerate(lines):
        for match in r_symbol.finditer(line):
            symbols.append((i, match.span()[0]))

        for match in r_numbers.finditer(line):
            numbers.append((i, match.span(), int(match.group())))

    for number in numbers:
        for symbol in symbols:
            for j in range(number[1][0], number[1][1]):
                if number[0] in range(symbol[0]-1, symbol[0]+2) and j in range(symbol[1]-1, symbol[1]+2):
                    sum += number[2]
                    break

    return sum


def part2(lines):
    sum = 0

    r_numbers = re.compile(r'(\d+)')
    r_gears = re.compile(r'(\*)')

    numbers = []
    gears = []

    for i, line in enumerate(lines):
        for match in r_gears.finditer(line):
            gears.append((i, match.span()[0]))

        for match in r_numbers.finditer(line):
            numbers.append((i, match.span(), int(match.group())))

    for gear in gears:
        neighbors = []
        for number in numbers:
            for j in range(number[1][0], number[1][1]):
                if number[0] in range(gear[0]-1, gear[0]+2) and j in range(gear[1]-1, gear[1]+2):
                    neighbors.append(number[2])
                    break
        if len(neighbors) == 2:
            sum += neighbors[0] * neighbors[1]

    return sum


if __name__ == '__main__':
    with open('Day3/input.txt', 'r') as f:
        lines = f.readlines()

    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
