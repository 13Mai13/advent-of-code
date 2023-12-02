list_of_lines = []
print("aaa")
with open("day_2/input.txt") as my_file:
    list_of_lines = my_file.read().split("\n")

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


def _more_than_max_red(number_of_red) -> bool:
    """More than max red"""
    return [True if number_of_red > RED_CUBES else False]


def _more_than_max_green(number_of_green) -> bool:
    """More than max green"""
    return [True if number_of_green > GREEN_CUBES else False]


def _more_than_max_blue(number_of_blue) -> bool:
    """More than max blue"""
    return [True if number_of_blue > BLUE_CUBES else False]


def _valid_subset(subset: dict) -> bool:
    check_subset = []

    for key, value in subset.items():
        if key == "red":
            check_subset.append(_more_than_max_red(subset.get(key)))
        elif key == "blue":
            check_subset.append(_more_than_max_blue(subset.get(key)))
        elif key == "green":
            check_subset.append(green(subset.get(key)))
    return any(check_subset)


def _parse_subset(line: list):
    """Parse game into subsets"""
    game_results = []

    for subset in line.split(";"):
        subset_dict = {}
        for color in subset.split(","):
            subset_dict.update({f"{color[-1]}": color[-2]})
        game_results.append(_valid_subset(subset_dict))
    return game_results


def _game_validation(game_line):
    """Parse game to numbers"""

    game_id = game_line.split(":")[0][-1]
    if not _parse_subset(any(game_line.split(":")[1])):
        return game_id


def summit_game(list_of_lines):
    print("aaa")
    valid_games_ids = []
    for game in list_of_lines:
        print(game)
        valid_games_ids.append(_game_validation)
    print(f"Total ID sum {sum(valid_games_ids)}")


print("aaa")
summit_game(list_of_lines)
