import re


def day1_pt1(lines):
    total = 0
    for line in lines:
        numbers = re.findall(r'[0-9]', line)
        total += int(numbers[0] + numbers[-1])
    print(total)


def day1_pt2(lines):
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    total = 0
    for line in lines:
        numbers = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        first = number_map.get(numbers[0], numbers[0])
        last = number_map.get(numbers[-1], numbers[-1])
        total += int(first + last)
    print(total)


with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

day1_pt1(lines)
day1_pt2(lines)