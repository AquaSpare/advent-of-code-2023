import re


def main():
    mapping = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    sum = 0

    regex = '(?=(one|two|three|four|five|six|seven|eight|nine|[123456789]))'

    with open('Day1/input.txt', 'r') as f:
        for line in f.readlines():
            matches = re.findall(regex, line)
            number = int(mapping[matches[0]] + mapping[matches[-1]])
            sum += number

    print(sum)


if __name__ == '__main__':
    main()
