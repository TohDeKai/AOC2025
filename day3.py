def lobby_pt1(puzzle):
    res = 0
    for bank in puzzle:
        bank = bank.strip()
        pointer, n = 0,len(bank)
        tens, ones = 0,0
        while pointer < n:
            if int(bank[pointer]) > tens and pointer < n - 1:
                tens = int(bank[pointer])
                ones = 0
            else:
                if int(bank[pointer]) > ones:
                    ones = int(bank[pointer])
            pointer += 1
        res += int(str(tens) + str(ones))
    return res

def lobby_pt2(puzzle):
    """
    Docstring for lobby_pt2
    
    :param puzzle: Description

    start from the first digit, test from first to last 12th, basically make sure there can be valid 12 numbers
    take the biggest
    start the next loop from the number next to the biggest
    """
    res = 0
    for bank in puzzle:
        bank = bank.strip()
        pointer, n = 0,len(bank)
        digits = 12
        prev_idx = -1
        joltage = ""
        while digits > 0:
            prev_idx += 1
            pointer = prev_idx 
            biggest = bank[pointer]
            while pointer < n - digits + 1:
                if int(bank[pointer]) > int(biggest):
                    biggest = bank[pointer]
                    prev_idx = pointer
                pointer += 1
            joltage = joltage + biggest
            digits -= 1
        res += int(joltage)
    return res


# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print(lobby_pt1(puzzle))
print(lobby_pt2(puzzle))