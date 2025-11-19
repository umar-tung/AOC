import sys

def create_block_view(raw_disk_map: str) -> list[str]:

    raw_disk_map_list = [x for x in raw_disk_map]

    block_view = []

    for index, character in enumerate(raw_disk_map):
        number = int(character)
        if index % 2 == 0:
            block_view.extend([f"{index//2}"]*number)
        else:
            block_view.extend(["."]*number)
            
    return block_view

def condense_block(block: list[str]) -> list[str]:

    beg = 0

    end = len(block) - 1

    # move beginning to the first empty index

    while beg < end:
        while beg < end and block[beg] != ".":
            beg+=1

        while beg < end and block[end] == ".":
            end -=1

        # make the swap and move the indices

        temp = block[beg]
        block[beg] = block[end]
        block[end] = temp

        beg +=1
        end -=1

    return block

def calculate_checksum(condensed_block: list[str]) -> int:

    total = 0
    for index, character in enumerate(condensed_block):
        if character == ".": continue 

        total += index * int(character)

    return total

if __name__ == "__main__":

    args = sys.argv[1:]

    file_path = args[0]

    with open(file_path) as file:

        raw_disk_map = file.readline().strip()

        block_view = create_block_view(raw_disk_map)
        
        condensed_block = condense_block(block_view)

        check_sum = calculate_checksum(condensed_block)

        print(f"{check_sum}")

        

