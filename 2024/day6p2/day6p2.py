import sys
import copy
from multiprocessing import Pool



args = sys.argv[1:]

file_path = args[0]


#visited_coords = set() # don't need, can just use X on the map

directions = {
    "<": (0,-1, "^"),
    "^": (-1, 0, ">"),
    ">": (0, 1, "v"),
    "v": (1, 0, "<"),
}

def find_guard(grid: list[list[str]]) -> tuple[int, int]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in directions:
                return row, col
    return -1, -1

def simulate(grid: list[list[str]]) -> tuple[int, set[tuple[int, int, str]]]:

    ori_guard_coord = find_guard(grid)

    guard_row, guard_col = ori_guard_coord

    visited = set()

    while 0 <= guard_row < len(grid) and 0 <= guard_col < len(grid[0]):
        change_row, change_col, change_dir = directions[grid[guard_row][guard_col]]
        
        potential_row, potential_col = guard_row + change_row, guard_col + change_col

        if not (0 <= potential_row < len(grid) and 0 <= potential_col < len(grid[0])):
            break

        # might need some change here with respect to the visited set
        if grid[potential_row][potential_col] == "#":
            grid[guard_row][guard_col] = change_dir 
            continue
        
        if (potential_row, potential_col, grid[guard_row][guard_col]) in visited:
            return 1, visited

        grid[potential_row][potential_col] = grid[guard_row][guard_col]
        visited.add((guard_row, guard_col, grid[guard_row][guard_col]))
        grid[guard_row][guard_col] = "X"

        guard_row, guard_col = potential_row, potential_col

    return 0, visited

# attempt to solve by adding an obstacle on the path at every step and simulating

if __name__ == "__main__":

    with open(file_path) as file:

        temp_grid = file.readlines()

        grid = [list(x.strip()) for x in temp_grid]

        temp_grid = copy.deepcopy(grid)

        ori_guard_coord = find_guard(temp_grid)

        guard_coord = ori_guard_coord

        guard_row, guard_col = guard_coord

        distinct_count = 0
        visited_cycle = set(guard_coord)
        
        _, visited = simulate(temp_grid)

        total = 0

        print(len(visited))

        for row, col, direction in visited:
            temp_grid = copy.deepcopy(grid)
            temp_grid[row][col] = "#"
            score, _ = simulate(temp_grid)
            # for line in temp_grid:
            #     print(line)
            total += score

        print(total)

