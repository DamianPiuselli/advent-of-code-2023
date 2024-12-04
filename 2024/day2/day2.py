with open("2024\day2\input.txt") as f:
    data = f.readlines()

    values = [[int(val) for val in line.split()] for line in data]


def is_safe(vals):

    differences = [vals[i] - vals[i - 1] for i in range(1, len(vals))]

    # check if all differences are positive or all are negative
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        # check if all differences at most 3 and at least 1
        if all(diff <= 3 and diff >= 1 for diff in differences):
            return True
        if all(diff <= -1 and diff >= -3 for diff in differences):
            return True
        else:
            return False

    else:
        return False


def is_safe_with_dampener(vals):
    # make every combination of removing one item from a list
    for i in range(len(vals)):
        temp = vals.copy()
        temp.pop(i)
        if is_safe(temp):
            return True
    return False


print(f"safe without dampener {sum([is_safe(val) for val in values])}")
print(f"safe with dampener {sum([is_safe_with_dampener(val) for val in values])}")
