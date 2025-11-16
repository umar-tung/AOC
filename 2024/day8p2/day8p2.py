import sys
from functools import reduce


def collect_antennae(grid: list[list[str]]) -> dict[str,set[tuple[int, int]]]:

    antennae = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ".":
                continue

            cur_antenna = grid[row][col]

            if cur_antenna in antennae:
                antennae[cur_antenna].add((row, col))
            else:
                antennae[cur_antenna] = set([(row, col)])
    return antennae

def collect_antinodes(antennae_map: dict[str,set[tuple[int, int]]], grid_len: int, grid_height: int) -> dict[str,set[tuple[int, int]]]:

    antinode_map = {}
    for antenna_type in antennae_map.keys():
        antinode_map[antenna_type] = set()
        antennae_set = antennae_map[antenna_type]
        antennae_list = list(antennae_set)

        print(f"{antennae_list=}")
        for i in range(len(antennae_list)):
            for j in range(len(antennae_list)):
                if i == j: continue
                antinode_map[antenna_type] |= find_antinodes(antennae_list[i], antennae_list[j], grid_len, grid_height)

    return antinode_map

def find_antinodes(coord1: tuple[int, int], coord2: tuple[int, int], grid_len: int, grid_height: int) -> set[tuple[int, int]]:

    antinodes = set()

    row_diff = coord1[0] - coord2[0]
    col_diff = coord1[1] - coord2[1]

    # pos antinodes
    curr_coord = coord1
    while 0 <= curr_coord[0] < grid_height and 0 <= curr_coord[1] < grid_len:
        antinodes.add(curr_coord)
        curr_coord = (curr_coord[0] + row_diff, curr_coord[1] + col_diff)

    row_diff = -row_diff
    col_diff = -col_diff

    # nodes in the other direction
    while 0 <= curr_coord[0] < grid_height and 0 <= curr_coord[1] < grid_len:
        antinodes.add(curr_coord)
        curr_coord = (curr_coord[0] + row_diff, curr_coord[1] + col_diff)

    antinodes.add(coord1)
    antinodes.add(coord2)

    return antinodes


if __name__ == "__main__":

    args = sys.argv[1:]

    file_path = args[0]

    with open(file_path) as file:

        grid = [list(x.strip()) for x in file.readlines()]

        antennae = collect_antennae(grid)
        print(f"{antennae=}")
        antinodes = collect_antinodes(antennae, len(grid), len(grid[0]))
        print(f"{antinodes=}")

    total = 0
    big_set = set()
    for nodes in antinodes.values():
        big_set |= nodes
    print(len(big_set))

