import sys

args = sys.argv[1:]

file_path = args[0]

with open(file_path) as file:

    grid = file.readlines()

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "A":
                continue

            # check for the diagonal M's and matching diagonal S's

            diag = {
                (-1, -1) : (1, 1), 
                (1, -1): (-1, 1), 
                (1, 1): (-1, -1),
                (-1, 1): (1, -1),
            }

            match_count = 0
            for M_coord, S_coord in diag.items():

                if not (0 <= row + M_coord[0] < len(grid) and 0 <= col + M_coord[1] < len(grid) and 0 <= row + S_coord[0] < len(grid) and 0 <= col + S_coord[1] < len(grid)):
                    continue
                if grid[row + M_coord[0]][col + M_coord[1]] == "M" and grid[row + S_coord[0]][col + S_coord[1]] == "S":
                    match_count +=1

            if match_count == 2:
                total +=1
    print(total)



