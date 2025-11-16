import sys

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


with open(file_path) as file:

    grid = file.readlines()

    grid = [list(x.strip()) for x in grid]

    guard_coord = find_guard(grid)

    guard_row, guard_col = guard_coord

    distinct_count = 0
    while 0 <= guard_row < len(grid) and 0 <= guard_col < len(grid[0]):

        change_row, change_col, change_dir = directions[grid[guard_row][guard_col]]
        
        potential_row, potential_col = guard_row + change_row, guard_col + change_col

        if not (0 <= potential_row < len(grid) and 0 <= potential_col < len(grid[0])):
            break

        if grid[potential_row][potential_col] == "#":
            grid[guard_row][guard_col] = change_dir 
            continue
        
        if grid[potential_row][potential_col] != "X":
            distinct_count +=1

        grid[potential_row][potential_col] = grid[guard_row][guard_col]
        grid[guard_row][guard_col] = "X"

        guard_row, guard_col = potential_row, potential_col

    print(distinct_count + 1)







