"""
Checks if numbers on left of | in input.txt are in the winning numbers on
the right of |. If there is a match, the score is 1 which is then doubled
for every subsequent match. Total is printed.
"""
import re


def main():
    total_score = 0
    with open("input.txt") as f:
        for line in f:
            winning_nums = re.findall(r"(?<=\:\s).*(?=\s\|)", line)[0]
            winning_nums = re.findall("[0-9]+", winning_nums)

            nums = re.findall(r"(?<=\|\s).*", line)[0]
            nums = re.findall("[0-9]+", nums)

            score = 0
            for num in nums:
                if num in winning_nums:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
                    continue
            total_score += score

    print(total_score)


if __name__ == "__main__":
    main()
