# create a dictionary of spaces to check
#
# store the entire map in memory
import math


def is_part_number(i: int, j: int, grid: list[list[str]]) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0

    if grid[i][j].isnumeric():
        k = j

        while k < len(grid[i]) and grid[i][k].isnumeric():
            k += 1

        num = int("".join(grid[i][j:k]))

        for x in range(j, k):
            grid[i][x] = "."

        for l in range(i - 1, i + 2):
            for m in range(j - 1, k + 1):
                if l < 0 or l >= len(grid):
                    continue
                if m < 0 or m >= len(grid[l]):
                    continue
                if not grid[l][m].isnumeric() and grid[l][m] != ".":
                    return num

    return 0


def check_gears_around(
    i: int,
    j: int,
    grid: list[list[str]],
    gear_coords: dict[tuple[int, tuple[int, int]], list[tuple[int, int]]],
) -> None:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    if grid[i][j].isnumeric():
        k = j

        while k < len(grid[i]) and grid[i][k].isnumeric():
            k += 1

        num = int("".join(grid[i][j:k]))

        for x in range(j, k):
            grid[i][x] = "."

        for l in range(i - 1, i + 2):
            for m in range(j - 1, k + 1):
                if l < 0 or l >= len(grid):
                    continue
                if m < 0 or m >= len(grid[l]):
                    continue
                if grid[l][m] == "*":
                    if (num, (i, j)) in gear_coords:
                        gear_coords[(num, (i, j))].append((l, m))
                    else:
                        gear_coords[(num, (i, j))] = [(l, m)]


def get_gear_ratio(
    i: int,
    j: int,
    grid: list[list[str]],
    gear_coords: dict[tuple[int, tuple[int, int]], list[tuple[int, int]]],
) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0
    # find all the adj numbers from the coord of the *
    adj_nums = []
    if grid[i][j] == "*":
        for num_key, gear_coord_list in gear_coords.items():
            for gear_coord in gear_coord_list:
                if gear_coord == (i, j):
                    adj_nums.append(num_key[0])

    return math.prod(adj_nums) if len(adj_nums) == 2 else 0


grid = []
with open("data.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        grid.append([])
        for character in line:
            if character != "\n":
                grid[i].append(character)

    gear_coords = {}

    total = 0
    for i, line in enumerate(grid):
        for j, character in enumerate(line):
            check_gears_around(i, j, grid, gear_coords)

    total = 0

    for i, line in enumerate(grid):
        for j, character in enumerate(line):
            total += get_gear_ratio(i, j, grid, gear_coords)

    # for x in grid:
    #     for y in x:
    #         if y != ".":
    #             print(y)

    print(total)
