import re

linetotals = []
with open("input.txt") as file:
    for line in file:
        nums = re.findall("[0-9]+", line)
        linetotals.append(10 * int(nums[0][0]) + int(nums[-1][-1]))
print(sum(linetotals))
