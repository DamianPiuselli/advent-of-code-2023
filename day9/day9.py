import numpy as np

with open("day9\input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    histories = [list(map(int, historie.split(" "))) for historie in lines]
    histories = histories


def reduce_seq(seq, accum=None):
    if not accum:
        accum = [seq]

    diff = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
    accum.append(diff)

    if not all([a == 0 for a in diff]):
        reduce_seq(diff, accum)

    return accum


def augment_seq_left(accum):
    for idx, seq in enumerate(reversed(accum)):
        if idx == 0:
            seq.append(0)
        else:
            seq.append(accum[-idx][-1] + seq[-1])
    return accum[0][-1]


def augment_seq_right(accum):
    for idx, seq in enumerate(reversed(accum)):
        if idx == 0:
            seq.insert(0, 0)
        else:
            seq.insert(0, -accum[-idx][0] + seq[0])
    return accum[0][0]


def extrapolate_left(seq):
    accum = reduce_seq(seq)
    return augment_seq_left(accum)


def extrapolate_right(seq):
    accum = reduce_seq(seq)
    return augment_seq_right(accum)


print(
    f"sum of extrapolated values (part1):{sum([extrapolate_left(hist) for hist in histories])}"
)
print(
    f"sum of extrapolated values (part2):{sum([extrapolate_right(hist) for hist in histories])}"
)
