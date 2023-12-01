import re
filepath = '01/day1_input.txt'

NUMBERS = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9}

def checknumbers(text):
    index = 10000
    first = ''
    for n in NUMBERS.keys():
        res = re.search(r"%s" %n, text)
        if res is not None:
            if res.start() < index:
                index = res.start()
                first = res.group()
    return first, index

def checknumbersRev(text):
    index = 10000
    first = ''
    for n in NUMBERS.keys():
        n_rev= n[::-1]
        res = re.search(r"%s" %n_rev, text)
        if res is not None:
            if res.start() < index:
                index = res.start()
                first = res.group()
    return first, index
        
def checkdigit(text):
    for i in range(0, len(text)):
            if text[i].isdigit():
                return text[i], i
    return '', 10000

def main():       
    with open(filepath) as f:
        lines = f.read().splitlines() 
    
    #print(lines)

    total = 0
    for l in lines:
        temp = ""
        text1, idx1 = checkdigit(l)
        text2, idx2 = checknumbers(l)

        if int(idx1) < idx2:
            #print(text1)
            temp += text1
        else:
            #print(text2)
            temp += str(NUMBERS.get(text2))

        text1, idx1 = checkdigit(l[::-1])
        text2, idx2 = checknumbersRev(l[::-1])

        if int(idx1) < idx2:
            #print(text1)
            temp += text1
        else:
            #print(text2[::-1])
            temp += str(NUMBERS.get(text2[::-1]))

        #print(int(temp))
        total += int(temp)

    print(total)

if __name__ == "__main__":
    main()