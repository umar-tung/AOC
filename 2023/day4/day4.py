import math

with open("data.txt") as file:
    score = 0
    additional_copies: dict[int, int] = {}

    max_game_num = 0
    for line in file:
        game_data, data = line.split(": ")

        game_num = int(game_data.split()[1])

        max_game_num = max(game_num, max_game_num)

        winning_nums, my_nums = line.split("| ")

        winning_nums = winning_nums.split()
        my_nums = my_nums.split()

        winning_nums_set = set(winning_nums)

        matching_nums = 0
        for num in my_nums:
            if num in winning_nums_set:
                matching_nums += 1

        if game_num not in additional_copies:
            additional_copies[game_num] = 0
        if matching_nums > 0:
            score_this_card = math.pow(2, matching_nums - 1)
            for i in range(game_num + 1, game_num + int(matching_nums) + 1):
                if i in additional_copies:
                    additional_copies[i] += additional_copies[game_num] + 1
                else:
                    additional_copies[i] = additional_copies[game_num] + 1

    total_copies = max_game_num
    for game, num_copies in additional_copies.items():
        if game <= max_game_num:
            total_copies += num_copies

    print(int(total_copies))
