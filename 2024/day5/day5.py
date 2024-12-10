with open(r"2024\day5\input.txt") as f:
    data = f.read().splitlines()

    order = data[: data.index("")]
    manuals = data[data.index("") + 1 :]

    # split at | for each string in list and format as int the substring after and before |
    order = [tuple(map(int, i.split("|"))) for i in order]
    manuals = [list(map(int, i.split(","))) for i in manuals]

    def ordered(manuals, order):
        output = []

        for manual in manuals:
            in_order = True
            for before, after in order:
                if before in manual and after in manual:
                    if manual.index(before) > manual.index(after):
                        in_order = False
                        break
            if in_order:
                output.append(manual[len(manual) // 2])
        return output

    def is_ordered(manual, order):

        in_order = True
        for before, after in order:
            if before in manual and after in manual:
                if manual.index(before) > manual.index(after):
                    in_order = False
                    break
        return in_order

    def order_manual(manual, order):
        if is_ordered(manual, order):
            return manual[len(manual) // 2]

        else:
            for before, after in order:
                if before in manual and after in manual:
                    if manual.index(before) > manual.index(after):
                        manual[manual.index(before)], manual[manual.index(after)] = (
                            manual[manual.index(after)],
                            manual[manual.index(before)],
                        )
            return order_manual(manual, order)

    print(sum(ordered(manuals, order)))
    print(
        sum(
            [
                order_manual(manual, order)
                for manual in manuals
                if not is_ordered(manual, order)
            ]
        )
    )
