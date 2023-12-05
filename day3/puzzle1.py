"""
Finds any number in input.txt that is adjacent to a symbol, including
diagonally, and sums the total.
"""
import re

NONSYMBOLS = "0123456789. \n"


def main():
    total = 0
    with open("input.txt") as f:
        text = [line for line in f]

    p = re.compile("[0-9]+")
    for line in range(len(text)):
        for search in p.finditer(text[line]):
            if AdjacentSymbols(text, line, search.start(), search.end()):
                total += int(search.group())
    print(total)


def AdjacentSymbols(text, line, numStart, numEnd):
    for i in range(-1, 2):
        j = 0
        while j < numEnd - numStart + 2:
            if text[line + i][numStart - 1 + j] not in NONSYMBOLS:
                return True
            j += 1
    return False


if __name__ == "__main__":
    main()
