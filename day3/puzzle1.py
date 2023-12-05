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
                print(search.group())
                total += int(search.group())
    print(total)


def AdjacentSymbols(text, line, numStart, numEnd):
    # Checks if any symbols are in the surrounding spaces about text.

    # Checks for symbols before number.
    if numStart != 0:
        if text[line][numStart - 1] not in NONSYMBOLS:
            return True

    # Check for symbols after number.
    if numEnd != len(text[line]) - 1:
        if text[line][numEnd] not in NONSYMBOLS:
            return True

    # Checks for symbols on line above.
    if line != 0:
        for i in range(numEnd - numStart + 2):
            try:
                if text[line - 1][numStart - 1 + i] not in NONSYMBOLS:
                    return True
            except IndexError:
                continue

    # Checks for symbols on line below.
    if line != len(text):
        for i in range(numEnd - numStart + 2):
            try:
                if text[line + 1][numStart - 1 + i] not in NONSYMBOLS:
                    return True
            except IndexError:
                continue

    return False


if __name__ == "__main__":
    main()
