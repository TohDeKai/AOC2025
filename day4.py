def count_adjacent_rolls(puzzle, x, y):
    height, width = len(puzzle), len(puzzle[0])
    count = 0

    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1),
        (-1, -1), (1, -1),
        (-1, 1), (1, 1),
    ]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < width and 0 <= ny < height:
            if puzzle[ny][nx] == "@":
                count += 1

    return count


def printing_department_pt1(puzzle):
    height, width = len(puzzle), len(puzzle[0])
    accessible_rolls = 0

    for y in range(height):
        for x in range(width):
            if puzzle[y][x] == "@" and count_adjacent_rolls(puzzle, x, y) < 4:
                accessible_rolls += 1

    return accessible_rolls


def printing_department_pt2(puzzle):
    height, width = len(puzzle), len(puzzle[0])
    accessible_rolls = 0

    while True:
        to_remove = []

        for y in range(height):
            for x in range(width):
                if puzzle[y][x] == "@" and count_adjacent_rolls(puzzle, x, y) < 4:
                    to_remove.append((x, y))

        if not to_remove:
            break

        accessible_rolls += len(to_remove)

        for x, y in to_remove:
            puzzle[y][x] = "."

    return accessible_rolls


with open("input.txt") as f:
    puzzle = [list(line.strip()) for line in f]

print(printing_department_pt1(puzzle))

# Make a copy because part 2 mutates the puzzle
with open("input.txt") as f:
    puzzle = [list(line.strip()) for line in f]

print(printing_department_pt2(puzzle))