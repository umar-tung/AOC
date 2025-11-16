import sys


operations = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
        "||": lambda x, y: int(f"{str(x)}{str(y)}")
        }


def reachable_target(target: int, accum: int, nums: list[int]) -> bool:
    
    if accum > target:
        return False
    if len(nums) == 0:
        return accum == target

    reached_target = False

    for op in operations.values():

        if accum == 0:
            reached_target = reached_target or reachable_target(target, nums[0], nums[1:])
        else:
            reached_target = reached_target or reachable_target(target, op(accum, nums[0]), nums[1:])

    return reached_target


def parse_line(line: str) -> tuple[int, list[int]]:

    raw_target, raw_numbers = line.split(":")

    return int(raw_target), [int(x) for x in raw_numbers.strip().split(" ")]


if __name__ == "__main__":
    args = sys.argv[1:]

    file_path = args[0]

    with open(file_path) as file:

        total = 0
        for line in file:
            target, nums = parse_line(line)
            if reachable_target(target, 0, nums):
                total += target

    print(total)

