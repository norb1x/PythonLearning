import re

def open_input(location) -> list:
    try:
        with open(location, 'r') as input_file:
            return input_file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {location}")
        return []

def process_multiplications(input_lines: list) -> int:
    valid_mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    total_sum = 0
    for line in input_lines:
        matches = re.findall(valid_mul_pattern, line)
        total_sum += sum(int(x) * int(y) for x, y in matches)
    return total_sum

file_path = r"input.txt"

input_lines = open_input(file_path)
if input_lines:
    result = process_multiplications(input_lines)
    print(f"The total sum of all valid multiplications is: {result}")
else:
    print("No content read from the file.")