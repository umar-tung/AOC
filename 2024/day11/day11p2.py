from collections import defaultdict
import sys

def sanitize_zeros(num_str: str) -> str:
    i = 0
    while i < len(num_str) and num_str[i] == "0":
        i+=1
    
    return "0" if i == len(num_str) else num_str[i:]

def simulate(stone_map: dict[int, int]) -> dict[int, int]:
    new_stone_map = defaultdict(int)
    for stone, count in stone_map.items():
        #print(f"{stone=} {count=}")

        if stone == 0:
            new_stone_map[1] += count
            continue

        if len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            lstone = int(str_stone[:len(str_stone)//2])
            rstone = int(str_stone[len(str_stone)//2:])

            new_stone_map[lstone] += count
            new_stone_map[rstone] += count
            continue

        new_stone_map[stone*2024] += count
    return new_stone_map

if __name__ == "__main__":
    args = sys.argv[1:]

    file_name = args[0]

    with open(file_name) as file:

        stones = file.readline().strip().split(" ")

        stone_map = defaultdict(int)

        for stone in stones:
            stone_map[int(stone)] += 1

        for i in range(75):
            stone_map = simulate(stone_map)

        count = 0
        for stone_count in stone_map.values():
            count += stone_count

        print(count)




