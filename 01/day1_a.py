def checkdigit(line):
    for i in range(0, len(line)):
        if line[i].isdigit():
            return line[i]


def main():
    filepath = "01/day1_input.txt"
    with open(filepath) as f:
        lines = f.read().splitlines()

    result = 0
    for l in lines:
        temp = ""
        temp += checkdigit(l)
        temp += checkdigit(l[::-1])
        result += int(temp)
    print(result)


if __name__ == "__main__":
    main()
