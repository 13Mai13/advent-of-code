list_of_lines = []

with open("day_2/input.txt") as my_file:
    list_of_lines = my_file.read().split("\n")


def _parse_subset(line: list):
    """Get Max of each game"""

    max_red = 0
    max_blue = 0
    max_green = 0

    for subset in line.split(";"):
        for color in subset.split(","):
            color_name = color.split(" ")[-1]
            quantity = int(color.split(" ")[-2])

            if color_name == "red" and quantity > max_red:
                max_red = quantity
            elif color_name == "blue" and quantity > max_blue:
                max_blue = quantity
            elif color_name == "green" and quantity > max_green:
                max_green = quantity
    return max_red * max_blue * max_green


def summit_game(list_of_lines):
    valid_games_ids = []
    for game in list_of_lines:
        valid_games_ids.append(_parse_subset(game.split(":")[1]))
    print(f"Total sum {sum(valid_games_ids)}")


summit_game(list_of_lines)
