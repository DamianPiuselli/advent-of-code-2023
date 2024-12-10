with open(r"2024\day4\input.txt") as f:
    data = [line.strip() for line in f.readlines()]


### find the word XMAS in a crossword represented as a list of chars


def is_xmas(i, j, data=data):
    if data[i][j] != "X":
        return 0

    count = 0

    up = [(i - 1, j), (i - 2, j), (i - 3, j)]
    down = [(i + 1, j), (i + 2, j), (i + 3, j)]
    left = [(i, j - 1), (i, j - 2), (i, j - 3)]
    right = [(i, j + 1), (i, j + 2), (i, j + 3)]
    up_left = [
        (i - 1, j - 1),
        (i - 2, j - 2),
        (i - 3, j - 3),
    ]
    up_right = [
        (i - 1, j + 1),
        (i - 2, j + 2),
        (i - 3, j + 3),
    ]
    down_left = [
        (i + 1, j - 1),
        (i + 2, j - 2),
        (i + 3, j - 3),
    ]
    down_right = [
        (i + 1, j + 1),
        (i + 2, j + 2),
        (i + 3, j + 3),
    ]

    directions = [up, down, left, right, up_left, up_right, down_left, down_right]

    for direction in directions:
        # check if coordinates in direction are out of bounds
        if any(
            [
                x < 0 or x >= len(data) or y < 0 or y >= len(data[x])
                for x, y in direction
            ]
        ):
            continue
        if "".join([data[x][y] for x, y in direction]) == "MAS":
            count += 1
    return count


print(sum([is_xmas(i, j) for i in range(len(data)) for j in range(len(data[i]))]))


def is_xmas2(i, j, data=data):
    if data[i][j] != "A":
        return 0

    positions = [(i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1)]

    if any(
        [x < 0 or x >= len(data) or y < 0 or y >= len(data[x]) for x, y in positions]
    ):
        return 0

    w = [0, 0]
    w[0] = data[i - 1][j - 1] + data[i][j] + data[i + 1][j + 1]
    w[1] = data[i + 1][j - 1] + data[i][j] + data[i - 1][j + 1]

    if w.count("MAS") + w.count("SAM") == 2:
        return 1

    return 0


print(sum([is_xmas2(i, j) for i in range(len(data)) for j in range(len(data[i]))]))
