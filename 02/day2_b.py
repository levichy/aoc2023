def checkMinCubes(current_game):
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for draw in current_game:
        draw = draw.split(",")
        for pair in draw:
            pair = pair.split()
            num = int(pair[0])
            colour = pair[1]
            if num > int(min_cubes[colour]):
                min_cubes[colour] = num
    return min_cubes


def main():
    filepath = "02/day2_input.txt"
    with open(filepath) as f:
        lines = f.read().splitlines()

    power = 0
    for l in lines:
        current_game = l.split(":")[1].split(";")
        min_cubes = checkMinCubes(current_game)
        power += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    print(power)


if __name__ == "__main__":
    main()
