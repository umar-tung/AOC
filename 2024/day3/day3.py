import sys
import re


args = sys.argv[1:]


file_path = args[0]


# given a string check if it is do()


with open(file_path) as file:

    mul_flag = True
    total = 0
    for line in file:
        for index, character in enumerate(line):
            
            if index+4 < len(line) and line[index:index+4] == "do()":
                mul_flag = True
                continue

            if index+7 < len(line) and line[index:index+7] == "don't()":
                mul_flag = False
                continue

            if not mul_flag:
                continue

            match = re.match(r"mul\((\d+),(\d+)\)", line[index:])

            if match:
                total += int(match.group(1))*int(match.group(2))

    print(total)






