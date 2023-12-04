import re

COLOURS = ["red", "green", "blue"]
MAX = [12, 13, 14]


def main():
    score = 0
    with open("input.txt") as f:
        for line in f:
            gameNo = re.findall(r"(?<=Game\s)[0-9]+", line)[0]
            gameScore = int(gameNo)

            for i in line.split(";"):
                search = FindColours(i)

                if any([int(search[j]) > MAX[j] for j in range(len(search))]):
                    gameScore = 0
                    break
            score += gameScore
    print(score)


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
