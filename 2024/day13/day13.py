def solve(x_a, y_a, x_b, y_b, T_x, T_y):

    # Expressions for k_a and k_b
    k_a = (T_x * y_b - T_y * x_b) / (x_a * y_b - x_b * y_a)
    k_b = (-T_x * y_a + T_y * x_a) / (x_a * y_b - x_b * y_a)

    _k_a = int(k_a)
    _k_b = int(k_b)

    # test solutions
    if T_x == _k_a * x_a + _k_b * x_b and T_y == _k_a * y_a + _k_b * y_b:
        return _k_a, _k_b
    else:
        return None


import re

pattern1 = r"X\+(\d+), Y\+(\d+)"
pattern2 = r"X\=(\d+), Y\=(\d+)"

cost_a = 3
cost_b = 1

total_cost = 0

with open(r"2024\day13\input.txt") as f:
    lines = f.read().strip().splitlines()

    # Extracting the values 4 lines at a time
    for i in range(0, len(lines), 4):
        match1 = re.search(pattern1, lines[i])
        x_a, y_a = int(match1.group(1)), int(match1.group(2))

        match2 = re.search(pattern1, lines[i + 1])
        x_b, y_b = int(match2.group(1)), int(match2.group(2))

        match3 = re.search(pattern2, lines[i + 2])
        T_x, T_y = int(match3.group(1)), int(match3.group(2))

        solution = solve(x_a, y_a, x_b, y_b, T_x, T_y)

        if solution:
            k_a, k_b = solution
            cost = k_a * cost_a + k_b * cost_b
            total_cost += cost

            print(f"Solution of eq{i//4}: {k_a, k_b}  Cost: {cost}")
print(f"Total cost: {total_cost}")


total_cost = 0

with open(r"2024\day13\input.txt") as f:
    lines = f.read().strip().splitlines()

    # Extracting the values 4 lines at a time
    for i in range(0, len(lines), 4):
        match1 = re.search(pattern1, lines[i])
        x_a, y_a = int(match1.group(1)), int(match1.group(2))

        match2 = re.search(pattern1, lines[i + 1])
        x_b, y_b = int(match2.group(1)), int(match2.group(2))

        match3 = re.search(pattern2, lines[i + 2])
        T_x, T_y = (
            int(match3.group(1)) + 10000000000000,
            int(match3.group(2)) + 10000000000000,
        )

        solution = solve(x_a, y_a, x_b, y_b, T_x, T_y)

        if solution:
            k_a, k_b = solution
            cost = k_a * cost_a + k_b * cost_b
            total_cost += cost

            print(f"Solution of eq{i//4}: {k_a, k_b}  Cost: {cost}")
print(f"Total cost w/ corrections: {total_cost}")
