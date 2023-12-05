"""
A number of red, green and blue cubes are drawn from a bag. Given the amount
shown, what is the minimum amount of cubes of each colour that could be in 
the bag. Multiply numbers together and print total. 
"""
import re

COLOURS = ["red", "green", "blue"]
MAX = [12, 13, 14]


def main():
    totalPower = 0
    with open("input.txt") as f:
        for line in f:
            colourCount = [[] for i in range(len(COLOURS))]
            for i in line.split(";"):
                search = FindColours(i)

                for j in range(len(search)):
                    colourCount[j].append(int(search[j]))

            minCubes = [max(i) for i in colourCount]

            power = 1
            for i in minCubes:
                power *= i

            totalPower += power

    print(totalPower)


def FindColours(text):
    search = []
    for j in range(len(COLOURS)):
        regex = "[0-9]+(?= {})".format(COLOURS[j])
        s = re.findall(regex, text)
        try:
            search.append(s[0])
        except IndexError:
            search.append("0")
    return search


if __name__ == "__main__":
    main()
