with open("2024\day1\input.txt") as f:
    data = f.readlines()

    values = [line.split() for line in data]
    lv = [int(i[0]) for i in values]
    rv = [int(i[1]) for i in values]
    lv.sort(), rv.sort()

    print(sum([abs(l - r) for l, r in zip(lv, rv)]))


def similarity(lv, rv):
    similarity = 0
    for l in lv:
        k = 0
        for r in rv:
            if l == r:
                k += 1
        similarity += k * l
    return similarity


print(similarity(lv, rv))
