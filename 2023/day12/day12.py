import itertools


def parse_input(path):
    with open(path, "r") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]
        sequences, groups = [], []

        for line in lines:
            sequences.append(line[0])
            groups.append([int(g) for g in line[1].split(",")])

    return sequences, groups


def unique_permutations_from_group(group):
    _permutations = set(itertools.permutations(group))
    _str_permutations = []

    for p in _permutations:
        _str = ""
        for num in p:
            _str += num * "#" + "."

        _str_permutations.append(_str[:-1])

    return _str_permutations


def match_permutation(seq, str_perm):
    if len(seq) != len(str_perm):
        return False

    for s, p in zip(seq, str_perm):
        if s == "#" and p == ".":
            return False

    return True


def count_arrangements(sequence, group):
    str_permutations = unique_permutations_from_group(group)
    count = 0

    for str_perm in str_permutations:
        if match_permutation(sequence, str_perm):
            count += 1

    return count


if __name__ == "__main__":
    sequences, groups = parse_input("day12/test.txt")

    _str_permutations = unique_permutations_from_group(groups[1])
    print(sequences[1], _str_permutations)
    for _str in _str_permutations:
        print(match_permutation(sequences[1], _str))
