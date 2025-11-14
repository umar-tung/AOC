import sys
from collections import defaultdict

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

with open(file_path) as file:


    # read in all the rules

    rules = defaultdict(dict)

    for line in file:

        if not line.strip():
            break

        parse_rule(rules, line)

    total = 0
    for line in file:
        total += calc_line_value(rules, line)
    print(total)


