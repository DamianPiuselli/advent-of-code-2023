import re
from itertools import product

with open(r"2024\day7\input.txt") as f:
    # first value is the test value.
    calibration_data = [list(map(int, re.findall(r"\d+", line))) for line in f]


def valid_equation(data):
    test_val = data[0]
    equation_values = data[1:]
    possible_symbols = "+*|"
    number_of_symbols = len(equation_values) - 1

    # all combinations of symbols of number_of_symbols length
    for operations in product(possible_symbols, repeat=number_of_symbols):
        value = equation_values[0]
        for i, operation in enumerate(operations):
            if operation == "+":
                value += equation_values[i + 1]
            if operation == "*":
                value *= equation_values[i + 1]
            if operation == "|":
                value = int(str(value) + str(equation_values[i + 1]))
            if value > test_val:
                return 0
        if value == test_val:
            return test_val
    return 0


print(sum(valid_equation(data) for data in calibration_data))
