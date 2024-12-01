def galaxy_positions(universe):
    galaxy_positions = {}
    for y, row in enumerate(universe):
        for x, cell in enumerate(row):
            if cell == "#":
                galaxy_positions[len(galaxy_positions) + 1] = (x, y)
    return galaxy_positions


def find_empty_row(universe):
    empty_rows_y_index = []
    for y, row in enumerate(universe):
        if all(cell == "." for cell in row):
            empty_rows_y_index.append(y)
    return empty_rows_y_index


def find_empty_column(universe):
    empty_columns_x_index = []
    for x in range(len(universe[0])):
        if all(row[x] == "." for row in universe):
            empty_columns_x_index.append(x)
    return empty_columns_x_index


def shortest_path(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


def update_positions(
    positions, empty_rows_y_index, empty_columns_x_index, expansion_rate=1
):
    updated_positions = positions.copy()
    for i, pos in positions.items():
        x, y = pos
        x_, y_ = 0, 0
        for empty_row in empty_rows_y_index:
            if y > empty_row:
                y_ += expansion_rate
        for empty_column in empty_columns_x_index:
            if x > empty_column:
                x_ += expansion_rate
        updated_positions[i] = (x + x_, y + y_)
    return updated_positions


with open("day11/input.txt") as f:
    universe = [list(line.strip()) for line in f]

positions = galaxy_positions(universe)
empty_rows_y_index = find_empty_row(universe)
empty_columns_x_index = find_empty_column(universe)


positions_1 = update_positions(positions, empty_rows_y_index, empty_columns_x_index)
path_lengths_1 = {}

for i in positions_1:
    for j in positions_1:
        if i != j and (i, j) not in path_lengths_1 and (j, i) not in path_lengths_1:
            path_lengths_1[(i, j)] = shortest_path(positions_1[i], positions_1[j])

print(f"part 1: {sum(path_lengths_1.values())}")


positions_2 = update_positions(
    positions, empty_rows_y_index, empty_columns_x_index, expansion_rate=1000000 - 1
)
path_lengths_2 = {}

for i in positions_2:
    for j in positions_2:
        if i != j and (i, j) not in path_lengths_2 and (j, i) not in path_lengths_2:
            path_lengths_2[(i, j)] = shortest_path(positions_2[i], positions_2[j])

print(f"part 2: {sum(path_lengths_2.values())}")
