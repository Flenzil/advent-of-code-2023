"""
Finds any instances of * in input.txt that is adjacent to exactly two numbers, including
diagonally, multiplies the numbers and returns the sum over the whole text.
"""
import re

NUMBERS = "0123456789"


def main():
    total = 0
    with open("input.txt") as f:
        text = [line for line in f]

    p = re.compile(r"\*")

    for line in range(len(text)):
        for search in p.finditer(text[line]):
            adjacentNums = AdjacentNums(text, line, search.start())

            if len(adjacentNums) == 2:
                total += int(adjacentNums[0]) * int(adjacentNums[1])

    print(total)


def AdjacentNums(text, line, char):
    # Returns numbers around char.

    # Check for numbers before char.
    adjacentNums = []
    if char != 0:
        if text[line][char - 1] in NUMBERS:
            num, _ = SearchForNums(text, line, char - 1)
            adjacentNums.append(num)

    # Check for numbers after char.
    if char != len(text[line]) - 1:
        if text[line][char + 1] in NUMBERS:
            num, _ = SearchForNums(text, line, char + 1)
            adjacentNums.append(num)

    # Check for numbers on line above.
    if line != 0:
        i = 0
        while i < 3:
            try:
                if text[line - 1][char - 1 + i] in NUMBERS:
                    num, offset = SearchForNums(text, line - 1, char - 1 + i)
                    adjacentNums.append(num)
                    i += offset
                else:
                    i += 1
            except IndexError:
                continue

    # Check for numbers on line below.
    if line != len(text):
        i = 0
        while i < 3:
            try:
                if text[line + 1][char - 1 + i] in NUMBERS:
                    num, offset = SearchForNums(text, line + 1, char - 1 + i)
                    adjacentNums.append(num)
                    i += offset
                else:
                    i += 1
            except IndexError:
                continue

    return adjacentNums


def SearchForNums(text, line, char):
    # We have found part of a number: char. This function returns the rest
    # of the number.
    num = text[line][char]

    # First walk backward from match until numbers stop
    j = 1
    while text[line][char - j] in NUMBERS:
        num += text[line][char - j]
        j += 1
    # This will result in a reversed number, so reverse back.
    num = num[::-1]

    # Now walk forward from the match until numbers stop.
    j = 1
    while text[line][char + j] in NUMBERS:
        num += text[line][char + j]
        j += 1

    # To avoid the same number being picked up again, return j as an offset which
    # will skip the rest of the number.
    return num, j


if __name__ == "__main__":
    main()
