with open("2024\day3\input.txt") as f:
    lines = f.readlines()

    # use regular expressions to parse the following pattern mul(1-3digits,1-3digits)
    import re

    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    sum = 0
    for line in lines:
        # find all the matches
        matches = pattern.findall(line)

        for match in matches:
            sum += int(match[0]) * int(match[1])

    print(sum)

with open("2024\day3\input.txt") as f:
    inp = f.read()
    sum = 0

    substrings = "".join([s.split("don't()")[0] for s in inp.split("do()")])

    matches = pattern.findall(substrings)

    for match in matches:
        sum += int(match[0]) * int(match[1])

    print(sum)
