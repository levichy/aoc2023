MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


def checkIfPossible(current_game):
    for draw in current_game:
        draw = draw.split(",")
        for pair in draw:
            pair = pair.split()
            num = int(pair[0])
            colour = pair[1]
            if num > MAX_CUBES[colour]:
                return False
    return True


def main():
    filepath = "02/day2_input.txt"
    with open(filepath) as f:
        lines = f.read().splitlines()

    game_id = 0
    sum_ids = 0
    for l in lines:
        game_id += 1
        possible = True
        current_game = l.split(":")[1].split(";")
        possible = checkIfPossible(current_game)
        if possible:
            sum_ids += game_id
    print(sum_ids)


if __name__ == "__main__":
    main()
