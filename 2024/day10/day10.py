import sys

def count_unique_path_trailheads(grid: list[str]) -> int:

    total_count = 0
    def dfs(coord: tuple[int, int], prev: int) -> None:

        row, col = coord

        if not (0 <= row < len(grid)):
            return
        
        if not(0 <= col < len(grid[0])):
            return

        cur_val = int(grid[row][col])

        if cur_val != prev + 1:
            return
        
        if cur_val == 9:
            nonlocal total_count
            total_count +=1
            return

        for i, j in [(1,0), (-1, 0), (0,1), (0,-1)]:
            dfs((row+i, col+j), cur_val)

        return

    total_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "0": continue
            dfs((row, col), -1)
    return total_count


def count_trailheads(grid: list[str]) -> int:

    # dfs and keep track of the number of unique 9's you land on 
    # caveat: ensure we only move in directions that are one greater
    # optimization possible?: keep track of which trailheads are reachable from specific points?

    def dfs(coord: tuple[int, int], found_trailheads: set[tuple[int, int]], prev: int) -> None:

        row, col = coord

        if not (0 <= row < len(grid)):
            return
        
        if not(0 <= col < len(grid[0])):
            return

        cur_val = int(grid[row][col])

        if cur_val != prev + 1:
            return
        
        if cur_val == 9:
            found_trailheads.add((row, col))
            return

        for i, j in [(1,0), (-1, 0), (0,1), (0,-1)]:
            dfs((row+i, col+j), found_trailheads, cur_val)

        return

    trailhead_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "0": continue
            found_trailheads = set()
            dfs((row, col), found_trailheads, -1)
            trailhead_count += len(found_trailheads)
    return trailhead_count


if __name__ == "__main__":
    
    args = sys.argv[1:]

    file_name = args[0]

    with open(file_name) as file:

        grid = [x.strip() for x in file.readlines()]

        print(count_unique_path_trailheads(grid))


