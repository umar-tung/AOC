import sys
import re
import math

def process_arg(raw_str: str) -> tuple[int, int]:
    m = re.search(r'\w+: X.(\d+), Y.(\d+)', line)
    if m:
        return int(m.group(1)), int(m.group(2))
    return 0, 0

def determine_cheapest(claw_machine: list[tuple[int, int]]):
    print(claw_machine)

    a_x, a_y = claw_machine[0]
    b_x, b_y = claw_machine[1]
    prize_x, prize_y = claw_machine[2]

    min_cost = math.inf
    for j in range(101):
        for i in range(101):
            cur_x, cur_y = i*a_x + j * b_x , i*a_y + j* b_y

            if cur_x == prize_x and cur_y == prize_y:
                print(f"{i=} {j=}")
                min_cost = min(i*3 + j, min_cost)

            # if cur_x > prize_x or cur_y > prize_y:
            #     break

    print(f"{min_cost=}")
    return min_cost

# 3A + 1B = C but there is only one solution because there are 2 lines
# A * A_X + B * B_X = ZX
# A * A_Y + B * B_Y = ZY

# B = (ZY - A* A_Y)/B_Y

# A * A_X + (ZY - A * A_Y)/B_Y * B_X = ZX
# A * A_X + (B_X * ZY - A * A_Y * B_X)/B_Y = ZX
# A * A_X + B_X*ZY/B_Y - A*A_Y*B_X/B_Y
# A * A_X - A*A_Y*B_X/B_Y = ZX - B_X*ZY/B_Y
# A = (ZX - B_X*ZY/B_Y)/(A_X - A_Y*B_X/B_Y)
# b=(py*ax-px*ay)/(by*ax-bx*ay) a=(px-b*bx)/ax

def determine_cheapest_p2(claw_machine: list[tuple[int, int]]):

    a_x, a_y = claw_machine[0]
    b_x, b_y = claw_machine[1]
    prize_x, prize_y = claw_machine[2]
    prize_x, prize_y = prize_x + 10000000000000, prize_y + 10000000000000

    print(claw_machine)


    B_presses = (prize_y*a_x-prize_x*a_y)/(b_y*a_x-b_x*a_y)


    A_presses = (prize_x - B_presses*b_x)/a_x

    if A_presses - math.floor(A_presses) != 0:
        return -1

    return A_presses * 3 + B_presses


if __name__ == "__main__":
    
    args = sys.argv[1:]

    file_name = args[0]

    with open(file_name) as file:

        claw_machines = []

        line = file.readline()
        while line:
            a_x, a_y = process_arg(line)
            line = file.readline()
            b_x, b_y = process_arg(line)
            line = file.readline()
            prize_x, prize_y = process_arg(line)
            prize_x, prize_y = prize_x , prize_y 

            claw_machines.append([(a_x, a_y), (b_x, b_y), (prize_x, prize_y)])

            line = file.readline() # expect empty line
            line = file.readline()

        
        total = 0
        for claw_machine in claw_machines:
            cost = determine_cheapest_p2(claw_machine)
            print(f"{cost=}")
            if cost == -1:
                continue
            total += cost

        print(f"{total=}")
