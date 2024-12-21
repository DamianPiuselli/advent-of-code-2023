D = [
    (i // 2 + 1 if i % 2 else 0, int(d))
    for i, d in enumerate(
        open(r"D:\documents\advent-of-code-2023\2024\day9\input.txt").read().strip(), 1
    )
]


def shift_data_to_empty_space(D):
    # find empty space from the front of the list

    for i, (empty_id, empty_size) in enumerate(D):
        if empty_id == 0:
            break

    # shift data from the back of the list to empty space

    for j, (data_id, data_size) in reversed(list(enumerate(D))):
        if data_id != 0:
            break

    if j + 1 == i:
        return True

    if empty_size == data_size:
        D[i] = (data_id, data_size)
        D[j] = (0, empty_size)

    elif empty_size > data_size:
        D[i] = (data_id, data_size)
        D[j] = (0, data_size)
        D.insert(i + 1, (0, empty_size - data_size))

    else:
        D[i] = (data_id, empty_size)
        D[j] = (data_id, data_size - empty_size)
        D.insert(j + 1, (0, empty_size))

    return False


def move_files_by_blocks(D):
    _len = len(D)

    for i in range(_len):
        if D[-1 - i][0] != 0:  # if block is not empty, iterating backwards
            data_id, data_size = D[-1 - i]
            for j in range(_len - i):
                if D[j][0] == 0:  # if block is empty, iterating forwards
                    empty_id, empty_size = D[j]
                    if empty_size == data_size:
                        D[j] = (data_id, data_size)
                        D[-1 - i] = (0, empty_size)
                        break
                    elif empty_size > data_size:
                        D[j] = (data_id, data_size)
                        D[-1 - i] = (0, data_size)
                        D.insert(j + 1, (0, empty_size - data_size))
                        break
                    else:
                        pass


def flatten(D):
    output = []
    for data_id, data_size in D:
        if data_id != 0:
            output = output + [data_id - 1] * data_size
    return output


def flatten_with_empty_space(D):
    output = []
    for data_id, data_size in D:
        if data_id != 0:
            output = output + [data_id - 1] * data_size
        else:
            output = output + ["."] * data_size
    return output


def score(D_flattened):
    return sum(i * d for i, d in enumerate(D_flattened) if d != ".")


# defrag = False

# while not defrag:
#     defrag = shift_data_to_empty_space(D)

# # score by summing the id at each position times the index
# print(score(flatten(D)))


move_files_by_blocks(D)
flat = flatten_with_empty_space(D)
print(flat)
print(score(flat))
