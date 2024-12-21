from collections import defaultdict

with open(r"2024/day8/input.txt", "r") as file:
    data = [line.strip() for line in file]

    antenas = defaultdict(list)

    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] != ".":
                antenas[data[x][y]].append((x, y))


antinodes = defaultdict(list)


def get_antinodes_positions(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    dx = x2 - x1
    dy = y2 - y1

    new_node = (x2 + dx, y2 + dy)

    return new_node


def coordinate_inside_bound(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])


for key, value in antenas.items():
    # for each possible pair of different antenas
    for i in range(len(value)):
        for j in range(i + 1, len(value)):
            new_node1 = get_antinodes_positions(value[i], value[j])
            new_node2 = get_antinodes_positions(value[j], value[i])

            if coordinate_inside_bound(*new_node1):
                antinodes[key].append(new_node1)

            if coordinate_inside_bound(*new_node2):
                antinodes[key].append(new_node2)


# pool all unique antinode positions
unique_antinodes = set()
for key, value in antinodes.items():
    for node in value:
        unique_antinodes.add(node)

print(len(unique_antinodes))


antinodes2 = set()


def add_antinodes_positions_with_resonance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    dx = x2 - x1
    dy = y2 - y1

    while True:
        new_node = (x2 + dx, y2 + dy)

        if not coordinate_inside_bound(*new_node):
            break

        antinodes2.add(new_node)

        x2, y2 = new_node


for key, value in antenas.items():
    # for each possible pair of different antenas
    for i in range(len(value)):
        for j in range(i + 1, len(value)):
            add_antinodes_positions_with_resonance(value[i], value[j])
            add_antinodes_positions_with_resonance(value[j], value[i])
# add all coordinates of antenas as antinodes
for key, value in antenas.items():
    for node in value:
        antinodes2.add(node)

print(len(antinodes2))
