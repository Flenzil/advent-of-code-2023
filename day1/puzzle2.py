"""
Finds first and last numbers in each line of file including those spelled out,
forms a two digit number from them and adds a running total
"""

import re
from word2number import w2n

NUMNAMES = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NUMS = "0123456789"


def main():
    linetotals = 0
    with open("input.txt") as file:
        for line in file:
            firstNum, lastNum = FindNumNames(line)
            linetotals += 10 * firstNum + lastNum
    print(linetotals)


def FindNumNames(text):
    firstStart = 100
    lastStart = -1
    firstNum = ""
    lastNum = ""
    patterns = NUMNAMES + [i for i in NUMS]

    for pattern in patterns:
        p = re.compile(pattern)

        for search in p.finditer(text):
            if search.start() < firstStart:
                firstStart = search.start()
                firstNum = search.group()

            if search.start() > lastStart:
                lastStart = search.start()
                lastNum = search.group()

    return w2n.word_to_num(firstNum), w2n.word_to_num(lastNum)


if __name__ == "__main__":
    main()
