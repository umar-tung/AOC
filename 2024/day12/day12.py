import sys

def collect_regions(grid: list[str]) -> list[set[tuple[int, int]]]:


    visited = set()

    def dfs(coord: tuple[int, int], plant_type: str, visited_region: set[tuple[int, int]]) -> None:
        row, col = coord

        if not (0 <= row < len(grid)):
            return
        if not (0 <= col < len(grid[0])):
            return

        if coord in visited_region:
            return

        if coord in visited:
            return

        if grid[row][col] != plant_type:
            return

        visited.add(coord)
        visited_region.add(coord)

        for i, j in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs((row+i, col+j), plant_type, visited_region)


    region_collection = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in visited:
                continue

            visited_region = set()
            dfs((row, col), grid[row][col], visited_region)
            region_collection.append(visited_region)
    return region_collection

def calculate_fence(region: set[tuple[int, int]]) -> int:

    # count the number of corners

    def count_corners(coord: tuple[int, int]) -> int:

        row, col = coord

        top = (row-1, col) in region
        right = (row, col+1) in region
        bottom = (row+1, col) in region
        left = (row, col-1) in region

        top_right = (row-1, col+1) in region
        bottom_right = (row+1, col+1) in region
        bottom_left = (row+1, col-1) in region
        top_left = (row-1, col-1) in region

        # check convex:

        corner_count = 0
        for i, j, k  in [(top, right, top_right), (right, bottom, bottom_right), (bottom, left, bottom_left), (left, top, top_left)]:
            # concave corner
            if i and j and not k:
                corner_count +=1
                continue

            # convex corner
            if not i and not j:
                corner_count +=1
                continue
        return corner_count

    total_corners = 0
    for row, col in region:
        total_corners += count_corners((row, col))

    return total_corners

if __name__ == "__main__":

    args = sys.argv[1:]

    file_name = args[0]

    with open(file_name) as file:

        grid = [x.strip() for x in file.readlines()]

        region_collection = collect_regions(grid)

        total = 0
        for region in region_collection:
            fence = calculate_fence(region)
            # print(f"{region=}")
            # print(f"{fence=}")
            total += len(region) * fence
        print(total)

