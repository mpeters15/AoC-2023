def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split('\n')

def parse_rounds_data(raw_rounds_data):
    rounds_data_list = []
    for raw_round in raw_rounds_data.split('; '):
        round_data = {}
        for color_count in raw_round.split(', '):
            count, color = color_count.split(' ')
            round_data[color] = int(count)
        rounds_data_list.append(round_data)
    return rounds_data_list

def process_input(raw_input_lines):
    game_rounds_data = {}
    for raw_input_line in raw_input_lines:
        game_name, raw_rounds_data = raw_input_line.split(': ')
        game_rounds_data[game_name] = parse_rounds_data(raw_rounds_data)
    return game_rounds_data

def calculate_powers(game_rounds_data):
    powers = []
    for game_name, rounds_data in game_rounds_data.items():
        max_red_count, max_green_count, max_blue_count = 0, 0, 0
        for round_data in rounds_data:
            count_red_cubes = round_data.get('red', 0)
            count_green_cubes = round_data.get('green', 0)
            count_blue_cubes = round_data.get('blue', 0)

            max_red_count = max(max_red_count, count_red_cubes)
            max_green_count = max(max_green_count, count_green_cubes)
            max_blue_count = max(max_blue_count, count_blue_cubes)

        power = max_red_count * max_green_count * max_blue_count
        powers.append(power)

    return powers

def filter_valid_game_numbers(game_rounds_data, max_red_cubes, max_green_cubes, max_blue_cubes):
    valid_game_numbers = set()
    invalid_game_numbers = set()

    for game_name, rounds_data in game_rounds_data.items():
        for round_data in rounds_data:
            count_red_cubes = round_data.get('red', 0)
            count_green_cubes = round_data.get('green', 0)
            count_blue_cubes = round_data.get('blue', 0)

            game_number = int(game_name.split(' ')[1])
            if (
                count_red_cubes <= max_red_cubes
                and count_green_cubes <= max_green_cubes
                and count_blue_cubes <= max_blue_cubes
            ):
                valid_game_numbers.add(game_number)
            else:
                invalid_game_numbers.add(game_number)

    return valid_game_numbers - invalid_game_numbers

def main():
    file_path = 'input.txt'
    raw_input_lines = read_input(file_path)
    game_rounds_data = process_input(raw_input_lines)

    max_red_cubes = 12
    max_green_cubes = 13
    max_blue_cubes = 14

    valid_game_numbers = filter_valid_game_numbers(game_rounds_data, max_red_cubes, max_green_cubes, max_blue_cubes)
    powers = calculate_powers(game_rounds_data)

    valid_game_numbers_sum = sum(valid_game_numbers)
    powers_sum = sum(powers)

    print(f"Sum of valid game numbers: {valid_game_numbers_sum}")
    print(f"Sum of powers: {powers_sum}")

if __name__ == "__main__":
    main()
