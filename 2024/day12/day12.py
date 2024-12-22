class Garden:
    def __init__(self):
        self.garden = dict()
        self.plot_patches = None

    @classmethod
    def from_file(cls, path):
        output = Garden()
        with open(path, "r") as file:
            for y, line in enumerate(file):
                for x, plant in enumerate(line.strip()):
                    output.garden[(x, y)] = plant
        return output

    def __str__(self):
        output = ""
        length = 1 + max(self.garden.keys(), key=lambda x: x[0])[0]

        for y in range(length):
            for x in range(length):
                output += self.garden[(x, y)]
            output += "\n"
        return output

    def __getitem__(self, key):
        return self.garden.get(key)

    def flood_fill(self, x, y, coords=None, plot_type=None):
        if coords is None:
            coords = set()
            plot_type = self.garden[(x, y)]
        if (x, y) in coords:
            return
        if self.garden.get((x, y)) != plot_type:
            return
        coords.add((x, y))
        self.flood_fill(x + 1, y, coords, plot_type)
        self.flood_fill(x - 1, y, coords, plot_type)
        self.flood_fill(x, y + 1, coords, plot_type)
        self.flood_fill(x, y - 1, coords, plot_type)
        return coords, plot_type

    def parse_plots(self):
        plots_patches = []
        available_plots = set(self.garden.keys())

        while available_plots:
            plot = available_plots.pop()

            patches_coords, plot_type = self.flood_fill(*plot)
            for plot in patches_coords:
                available_plots.discard(plot)
            plots_patches.append(patches_coords)

        self.plot_patches = plots_patches
        return plots_patches

    def score(self):
        if self.plot_patches is None:
            self.parse_plots()

        return sum(
            len(patch) * self.calculate_perimeter(patch) for patch in self.plot_patches
        )

    def score_bulk(self):
        if self.plot_patches is None:
            self.parse_plots()

        return sum(
            len(patch) * self.calculate_corners(patch) for patch in self.plot_patches
        )

    def calculate_perimeter(self, patch):
        perimeter = 0
        for x, y in patch:
            if (x + 1, y) not in patch:
                perimeter += 1
            if (x - 1, y) not in patch:
                perimeter += 1
            if (x, y + 1) not in patch:
                perimeter += 1
            if (x, y - 1) not in patch:
                perimeter += 1
        return perimeter

    def calculate_corners(self, patch):
        corners = 0

        for x, y in patch:
            # outer corners
            if (x + 1, y) not in patch and (x, y + 1) not in patch:
                corners += 1
            if (x - 1, y) not in patch and (x, y + 1) not in patch:
                corners += 1
            if (x + 1, y) not in patch and (x, y - 1) not in patch:
                corners += 1
            if (x - 1, y) not in patch and (x, y - 1) not in patch:
                corners += 1
            # inner corners
            if (
                (x + 1, y) in patch
                and (x, y + 1) in patch
                and (x + 1, y + 1) not in patch
            ):
                corners += 1
            if (
                (x - 1, y) in patch
                and (x, y + 1) in patch
                and (x - 1, y + 1) not in patch
            ):
                corners += 1
            if (
                (x + 1, y) in patch
                and (x, y - 1) in patch
                and (x + 1, y - 1) not in patch
            ):
                corners += 1
            if (
                (x - 1, y) in patch
                and (x, y - 1) in patch
                and (x - 1, y - 1) not in patch
            ):
                corners += 1
        return corners


garden = Garden.from_file(r"2024\day12\input.txt")
print(garden)
print(garden.score())
print(garden.score_bulk())
