import string
import collections

def is_valid_digit_char(char):
    return char in string.digits + ".\n "

def process_input(file_path):
    with open(file_path) as file:
        content = file.read()
    line_offset = content.find("\n") + 1
    content += " " * line_offset
    return content, line_offset

def calculate_sums_and_products(content, line_offset):
    sum_part1, sum_part2 = 0, 0
    position_count = collections.defaultdict(int)
    position_product = collections.defaultdict(lambda: 1)
    pos = 0

    while pos < len(content):
        if content[pos].isdigit():
            start_index = pos
            while content[pos].isdigit():
                pos += 1
            indices = list(range(start_index - 1 - line_offset, pos + 1 - line_offset)) 
            indices += [start_index - 1, pos] 
            indices += list(range(start_index - 1 + line_offset, pos + 1 + line_offset))
            if any(not is_valid_digit_char(content[x]) for x in indices):
                sum_part1 += int(content[start_index:pos])
            
            for x in indices:
                if content[x] == "*":
                    position_count[x] += 1
                    position_product[x] *= int(content[start_index:pos])

        pos += 1

    sum_part2 += sum(val for key, val in position_product.items() if position_count[key] == 2)

    return sum_part1, sum_part2

def main():
    content, line_offset = process_input("input.txt")
    sum_part1, sum_part2 = calculate_sums_and_products(content, line_offset)

    assert sum_part1 == 557705
    assert sum_part2 == 84266818

    print(sum_part1)
    print(sum_part2)

if __name__ == "__main__":
    main()
