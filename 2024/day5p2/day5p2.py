import sys
from collections import defaultdict
from functools import cmp_to_key

args = sys.argv[1:]

file_path = args[0]


# will add the raw rule string to the rules dictionary
# the rules dictionary key is the 
def parse_rule(rules: dict[int, dict[str, set[int]]], raw_rule: str) -> None:

    src, dst = [int(x) for x in raw_rule.split("|")]

    if src in rules:
        rules[src]["after"].add(dst)
    else:
        rules[src]["after"] = set([dst])
        rules[src]["before"] = set()

    if dst in rules:
        rules[dst]["before"].add(src)
    else:
        rules[dst]["before"] = set([src])
        rules[dst]["after"] = set()

def calc_line_value(rules: dict[int, dict[str, set[int]]], line: str) -> int:

        nums = [int(x) for x in line.split(",")]

        num_indexes = {}
        for index, num in enumerate(nums):
            num_indexes[num] = index

        # check whether the numbers are in the appropriate order
        for num in nums:
            for before_value in rules[num]["before"]:
                if before_value in num_indexes and num_indexes[before_value] > num_indexes[num]:
                    return 0
            for after_value in rules[num]["after"]:
                if after_value in num_indexes and num_indexes[after_value] < num_indexes[num]:
                    return 0

        return nums[len(nums)//2]

def value_after_change(rules: dict[int, dict[str, set[int]]], line: str) -> int:

        nums = [int(x) for x in line.split(",")]

        num_indexes = {}
        for index, num in enumerate(nums):
            num_indexes[num] = index

        def cmp(item1: int, item2: int) -> int:
            if item1 in rules:
                if item2 in rules[item1]["after"]:
                    return -1
                if item2 in rules[item1]["before"]:
                    return 1

            if item2 in rules:
                if item1 in rules[item2]["after"]:
                    return 1
                if item1 in rules[item2]["before"]:
                    return 1
            return 0
        sorted_nums = sorted(nums, key=cmp_to_key(cmp))

        return sorted_nums[len(nums)//2]

with open(file_path) as file:

    # read in all the rules

    rules = defaultdict(dict)

    for line in file:

        if not line.strip():
            break

        parse_rule(rules, line)

    total = 0
    for line in file:
        if calc_line_value(rules, line) != 0:
            continue

        total += value_after_change(rules, line)

    print(total)


