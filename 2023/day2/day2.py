# read in the data with it's format
#


max_amount = {
    "blue": 14,
    "red": 12,
    "green": 13,
}


def valid_line(line: str) -> bool:
    values = line.split(": ")[1]  # grab everything after game

    for pull in values.split("; "):
        for dice_amount in pull.split(", "):
            amount = int(dice_amount.split()[0].strip())
            dice_color = dice_amount.split()[1].strip()

            if amount > max_amount[dice_color]:
                return False

    return True


def min_power_line(line: str) -> int:
    values = line.split(": ")[1]  # grab everything after game
    local_max_amount = {
        "blue": 0,
        "red": 0,
        "green": 0,
    }

    for pull in values.split("; "):
        for dice_amount in pull.split(", "):
            amount = int(dice_amount.split()[0].strip())
            dice_color = dice_amount.split()[1].strip()

            if amount > local_max_amount[dice_color]:
                local_max_amount[dice_color] = amount

    res = 1

    for x in local_max_amount.values():
        res *= x

    return res


with open("data.txt", "r") as file:
    possible_games = 0

    for line in file:
        game_id = int(line.split(": ")[0].split()[1])

        possible_games += min_power_line(line)

    print(possible_games)
