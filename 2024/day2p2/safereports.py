
from itertools import pairwise

filename = "test.txt"

def comparison(nums, func):
    for i in range(1, len(nums)):
        if func(nums[i-1], nums[i]):
            return False
    return True

with open(filename) as file:
    score = 0
    for line in file:
        parsed_line = [int(x) for x in line.strip().split(" ")]

        for i in range(len(parsed_line)):
            removed_parsed_line = parsed_line[:i] + parsed_line[i+1:]
            if (comparison(removed_parsed_line, lambda x, y : x < y) or comparison(removed_parsed_line, lambda x, y: x > y)) and \
                comparison(removed_parsed_line, lambda x, y : abs(x - y) > 3 or abs(x - y) < 1):
                score +=1
                break

    print(score)


