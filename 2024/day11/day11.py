from collections import defaultdict


class StoneLine:
    def __init__(self):
        self.statues = defaultdict(int)

    def add(self, statue, frecuency=1):
        self.statues[statue] += frecuency

    @classmethod
    def from_input(cls, list_of_ints):
        output = StoneLine()
        for id in list_of_ints:
            output.add(int(id))

        return output

    def blink(self):
        output = StoneLine()

        for statue, frecuency in self.statues.items():

            if statue == 0:
                output.add(1, frecuency)

            elif len(str(abs(statue))) % 2 == 0:
                first_half, second_half = (
                    str(abs(statue))[: len(str(abs(statue))) // 2],
                    str(abs(statue))[len(str(abs(statue))) // 2 :],
                )
                output.add(int(first_half), frecuency)
                output.add(int(second_half), frecuency)
            else:
                output.add(statue * 2024, frecuency)

        return output

    def __str__(self):
        return str(self.statues)

    def __len__(self):
        return sum(self.statues.values())


input = "112 1110 163902 0 7656027 83039 9 74".split(" ")
line = StoneLine.from_input(input)


for i in range(1, 76):
    line = line.blink()
    if i in [25, 75]:
        print(f"after {i} blinks length: {len(line)}")
