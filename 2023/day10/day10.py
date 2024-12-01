with open("day10/input.txt") as f:
    maze = f.readlines()
    maze = [list(string.strip()) for string in maze]


def move(y_index, x_index):
    if maze[y_index][x_index] == "|":
        return y_index+1, x_index
    if maze[y_index][x_index] == "-":
        


