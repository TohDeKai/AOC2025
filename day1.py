def secret_entrance_pt1(puzzle):
    dial = 50
    password = 0 
    for line in puzzle:
        rotation = int(line[1:])
        if line[0] == "L":
            dial -= rotation
            while dial < 0:
                dial += 100
        elif line[0] == "R":
             dial += rotation
             while dial > 99:
                dial -= 100
        if dial == 0:
            password += 1
    
    return password

def secret_entrance_pt2(puzzle):
    dial = 50
    password = 0

    for line in puzzle:
        line = line.strip()
        rotation = int(line[1:])
        direction = 1 if line[0] == "R" else -1

        # simulate each click
        for _ in range(rotation):
            dial = (dial + direction) % 100
            if dial == 0:
                password += 1

    return password




# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print(secret_entrance_pt1(puzzle))
print(secret_entrance_pt2(puzzle))