import re


def main():
    total = 0
    mult = [1]
    with open("input.txt") as f:
        for line in f:
            winning_nums = re.findall(r"(?<=\:\s).*(?=\s\|)", line)[0]
            winning_nums = re.findall("[0-9]+", winning_nums)

            nums = re.findall(r"(?<=\|\s).*", line)[0]
            nums = re.findall("[0-9]+", nums)

            cards = 1
            for num in nums:
                if num in winning_nums:
                    cards += 1

            while len(mult) < cards:
                mult.append(1)

            add = mult[0]

            total += add
            for i in range(cards):
                mult[i] = mult[i] + add

            mult = mult[1:]

    print(total)


if __name__ == "__main__":
    main()
