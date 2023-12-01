import re

NUMBERS = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9}

def checkdigit(line, reverse):
    index = float('inf')
    num = ''

    # check for digit numbers
    for i in range(0, len(line)):
        if line[i].isdigit():
            index = i
            num = line[i]
            break
        
    # check for string numbers
    for n in NUMBERS.keys():
        if reverse:
            n = n[::-1]
        res = re.search(r"%s" %n, line)
        if res is not None:
            if res.start() < index:
                index = res.start()
                num = res.group()
    return num

def main():
    filepath = '01/day1_input.txt'
    with open(filepath) as f:
        lines = f.read().splitlines() 
    
    result = 0
    for l in lines:
        temp = ""

        # first digit
        first = checkdigit(l, reverse=False)
        if first.isdigit():
            temp += first
        else: 
            temp += str(NUMBERS.get(first))

        # last digit
        last = checkdigit(l[::-1], reverse=True)
        if last.isdigit():
            temp += last
        else: 
            temp += str(NUMBERS.get(last[::-1]))

        result += int(temp)    
    print(result)

if __name__ == "__main__":
    main()