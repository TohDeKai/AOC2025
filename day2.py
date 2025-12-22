def is_invalid(number):
    number = str(number)
    half = len(number) // 2
    return number[:half] == number[half:]

def giftshop_pt1(puzzle):
    result = 0
    for id_range in puzzle[0].split(","):
        bottom, top = id_range.split("-")
        bottom, top = int(bottom), int(top)
        for num in range(bottom, top+1):
            if is_invalid(num):
                result += num
    return result

import re


def giftshop_pt2(puzzle):
    pattern = re.compile(r'^(\d+)\1+$')
    result = 0
    for id_range in puzzle[0].split(","):
        bottom, top = id_range.split("-")
        bottom, top = int(bottom), int(top)
        for num in range(bottom, top+1):
            if pattern.fullmatch(str(num)):
                result += num
    return result


# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print(giftshop_pt1(puzzle))
print(giftshop_pt2(puzzle))