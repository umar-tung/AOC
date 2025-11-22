import sys
import math

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

def calc_segment(block: list[str], direction: int, index: int) -> tuple[str, int, int]:
    i = index
    length = 0
    while 0 <= i < len(block) and block[i] == block[index] :
        i += direction
        length +=1

    return block[index], length, i



def condense_block_p2(block: list[str]) -> list[str]:

    end = len(block) - 1

    while end >= 0:
        while end >= 0 and block[end] == ".":
            end -= 1

        end_character, end_length, new_end_index = calc_segment(block, -1, end)

        # look for the left most segment and replace with characters

        start = 0

        while start < new_end_index:
            while start < new_end_index and block[start] != ".":
                start += 1

            if start >= new_end_index:
                break

            start_character, start_length, new_start_index = calc_segment(block, 1, start)

            # replace the block if the segment fits
            if start_length >= end_length:
                i = 0
                while i < end_length:
                    block[start+i] = end_character
                    i+=1

                i = new_end_index + 1
                while i < len(block) and i <= new_end_index + end_length:
                    block[i] = "."
                    i+=1
                break

            start = new_start_index
        end = new_end_index

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
        
        #condensed_block = condense_block(block_view)

        condensed_block = condense_block_p2(block_view)

        check_sum = calculate_checksum(condensed_block)
        print(f"{check_sum}")
        

