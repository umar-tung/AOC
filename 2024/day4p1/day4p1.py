import sys

args = sys.argv[1:]

file_path = args[0]

# only need window of 8
# however, input seems small enough where we don't have to worry about that and can load
# it all into memory

directions = {
    'N': (-1,0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
    'NE': (-1, 1),
    'NW': (-1, -1),
    'SE': (1, 1),
    'SW': (1, -1),
}

def search_word(
    grid: list[str], 
    row: int, col: int, 
    direction: tuple[int, int], 
    word: str
) -> int:

    temp_row = row
    temp_col = col

    for index, character in enumerate(word):
        if not (0 <= temp_row < len(grid) and 0 <= temp_col < len(grid[0])) or \
            grid[temp_row][temp_col] != character:
            return 0

        temp_row, temp_col = temp_row + direction[0], temp_col + direction[1]

    # only return 1 if we made it to the end of the match
    return 1

with open(file_path) as file:

    grid = file.readlines()

    matches = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for direction in directions.values():
                matches += search_word(grid, row, col, direction, "XMAS")

    print(matches)

